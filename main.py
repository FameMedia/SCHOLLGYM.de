
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock, mainthread
from kivy.uix.screenmanager import *
from kivy.uix.image import *
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.properties import *
from kivy.uix.textinput import *
from kivy.uix.carousel import Carousel
from kivy.base import EventLoop
from kivy.uix.popup import Popup
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.actionbar import *
from kivy.uix.togglebutton import *
from kivy.graphics.instructions import Instruction, InstructionGroup
from kivy.core.window import Window
from kivy.uix.bubble import Bubble
import zipfile
import sys
import os
import threading
import time
import urllib
VPWEBSITE = "http://planung.schollgym.de"
MAINWEBSITE = "http://www.schollgym.de"
ZOOMWEBSITE = "http://zeitung.schollgym.de"
threads = []
menopen = False
inprogress = False



def exitapp(KEY=""):
    global threads
    for t in threads:
        try:
            t.stop()
        except:
            None
    sys.exit()

if os.path.isdir("/sdcard/.schollgymde") == False:
    os.makedirs("/sdcard/.schollgymde")

class ScreenManagerExtended(ScreenManager):
    background_color = ObjectProperty(Color(1,1,1,1))
class ScreenEx(Screen):
    background_color = ObjectProperty(Color(1,1,1,1))


class NewScreen(Screen):

    def setbg(self,widget,clr=(1,1,1,1)):
            print("setting color...")
            with widget.canvas.before:
                Color(clr[0],clr[1],clr[2],clr[3])  # green; colors range from 0-1 not 0-255
                self.rect = Rectangle(size=widget.size, pos=widget.pos)
                print("doing")
                widget.bind(size=self._update_rect, pos=self._update_rect)
            print("END OF SETTING COLOR")
    def _update_rect(self,instance,value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

def NewFloat(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayoutNew, self).__init__(**kwargs)



class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
    def setbg(self,widget,clr=(1,1,1,1)):
            print("setting color...")
            with widget.canvas.before:
                Color(clr[0],clr[1],clr[2],clr[3])  # green; colors range from 0-1 not 0-255
                self.rect = Rectangle(size=widget.size, pos=widget.pos)
                print("doing")
                widget.bind(size=self._update_rect, pos=self._update_rect)
            print("END OF SETTING COLOR")
    def _update_rect(self,instance,value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

def sleep(time,todo):
    Clock.schedule_once(todo,time)


def clone(_from,to):
    global connectdone
    #connectdone = False
    file = open(to,"wb")
    server.retrbinary("RETR "+_from,file.write)
    file.close()
    file = open(to,"r")
    t = file.read().replace("\\n","\n")
    file.close()
    #connectdone = True
    return t
def openmen(KEY=""):
    global titleflow, menopen,sidebar
    if menopen == True:
        closemen()
        menopen = False
        return 0
    menopen = True
    startprog("Menu Open")
    am = Animation(size=(52,52),duration=.2,t="in_out_circ")
    am2 = Animation(pos_hint={"x":0,"y":0},duration=.2 ,t="in_out_circ")
    am2.start(sidebar)
    am.start(titleflow)
    
def closemen():
    global titleflow
    stopprog()
    am = Animation(size=(48,48),duration=.2 ,t="in_out_circ")
    am2 = Animation(pos_hint={"x":-.8,"y":0},duration=.2 ,t="in_out_circ") 
    am2.start(sidebar)
    am.start(titleflow)
def goto_start(KEY=""):
    global sm, sc
    sc.size_hint = None,None
    sc.size = 48,48
    sc.pos_hint_x = None
    sc.pos_hint_y = None
    sc.pos = (int(winsize[0]/2)-24,int(winsize[1]/2)-24)
    am = Animation(size=(0,0))
    am &= Animation(pos=(winsize[0]/2,winsize[1]/2))
    am.start(sc)
    sleep(.8,goto_main)
def goto_main(KEY=""):
    global sm
    sm.current="mainscreen"
    sleep(.5,welcome)
def initfile(KEY=""):
    global threads
    """ This subprogram has to init all things """
    t = threading.Thread(target=vpthread)
    t.start()
    threads.append(t)

def vpthread():
    global done
    notshowp = False
    #speedtest
    try:
        start = time.clock()
        urllib.urlretrieve(VPWEBSITE,"/sdcard/.schollgymde/vp")
        end = time.clock()
        if end - start < 2:
            notshowp = True
    except:
         startprog("Offline")
         sleep(2,stopprog)
         return 0
    #end speedtest
    if notshowp:
        startprog("Lade Daten")
    else:
        startprog("Lade\nVertretungsplan")
    try:
        urllib.urlretrieve(VPWEBSITE,"/sdcard/.schollgymde/vp")
    except:
         startprog("Offline")
         sleep(2,stopprog)
         return 0
    if not notshowp:
        startprog("Lade\nHauptseite")
    try:
        urllib.urlretrieve(MAINWEBSITE,"/sdcard/.schollgymde/website")
    except:
        startprog("Offline")
        sleep(1,stopprog)
        return 0
    if not notshowp:
        startprog("Lade\nZeitungsartikel")
    urllib.urlretrieve(ZOOMWEBSITE,"/sdcard/.schollgymde/newspaper")
    stopprog()
def welcome(KEY=""):
    startprog("welcome")
    sleep(1,initfile)
    #sleep(3,welcome2)
def welcome2(KEY=""):
    startprog("Developer\nMode")
    sleep(3,stopprog)
def startprog(msg):
    global inprogress,proglabel,progmsg
    if inprogress:
        am = Animation(duration=.5,pos_hint={"x":.25,"y":1},color=(1,1,1,0),t="in_quad")
        am2 = Animation(duration=.5,pos_hint={"x":1.1,"y":.1},t="in_quad")
        am2.start(progimg)
        am.start(proglabel)
        sleep(.5,newprog)
        progmsg = msg
    else:
        proglabel.text = msg
        openprog()
    inprogress = True
    
def newprog(KEY=""):
    global proglabel,progmsg,progimg
    msg = progmsg
    proglabel.text = msg
    proglabel.pos_hint = {"x":.25,"y":-.4}
    progimg.pos_hint = {"x":1.1,"y":.1}
    openprog()
def openprog(KEY=""):
    global proglabel
    am = Animation(duration=.5,pos_hint={"x":.25,"y":0},color=(1,1,1,1),t="in_quad")
    am.start(proglabel)
    am2 = Animation(duration=.5,pos_hint={"x":.85,"y":.1},t="in_quad")
    am2.start(progimg)
def stopprog(KEY=""):
    global inprogress, proglabel
    inprogress = False
    am = Animation(duration=.5,pos_hint={"x":.25,"y":-.4},color=(1,1,1,0),t="in_quad")
    am.start(proglabel)
    am2 = Animation(duration=.5,pos_hint={"x":1.2,"y":0},t="in_quad")
    am2.start(progimg)
def openvp(KEY=""):
    global vpframe,vpopenbt,vpisopen
    if vpisopen:
        am = Animation(duration=1,pos_hint={"x":1,"y":1},t="in_out_circ")
        am2 = Animation(duration=1,pos_hint={"x":.85,"y":.78},t="in_out_circ")
        am.start(vpframe)
        am2.start(vpopenbt)
        vpisopen = False
        return 0

    vpisopen = True
    am = Animation(duration=1,pos_hint={"x":.3,"y":.3},t="in_out_circ")
    am2 = Animation(duration=1,pos_hint={"x":.15,"y":.18},t="in_out_circ")
    am.start(vpframe)
    am2.start(vpopenbt)
vpisopen = False
winsize = (Window.width,Window.height)
sm = ScreenManagerExtended()
mainscreen = NewScreen(name="mainscreen")
mainscreen.setbg(mainscreen,(1,1,1,1))
logonscreen = NewScreen(name="logonscreen")
sc = Image(source="school_white.png")
sm.add_widget(logonscreen)
logonscreen.add_widget(sc)
titlebar = RootWidget()
titlebar.setbg(titlebar,(63.0/255.0,81.0/255.0,181.0/255.0,1))
titlebar.size_hint = 1, .1
titlebar.pos_hint = {"x":0,"y":0.9}
vpopenbt = Button(background_normal="bag.png",background_down="bag.png", pos_hint={"x":.85,"y":.78},size_hint=(.15,.12),background_color=(63.0/255.0,81.0/255.0,181.0/255.0,1))
vpopenbt.bind(on_release=openvp)
vpframe = RootWidget()
vpframe.setbg(vpframe,(.9,.9,.9,1))
vpframe.size_hint = .7,.7
vpframe.pos_hint = {"x":1,"y":1}
vpinf = Label(text="KEIN\nVERTRETUNGSPLAN\nVORHANDEN",color=(0,0,0,1),font_size="20sp")
vpinf.pos_hint = {"x":0,"y":0}
vpframe.add_widget(vpinf)
mainscreen.add_widget(vpframe)
mainscreen.add_widget(vpopenbt)
titlelab = Label(text="SCHOLLGYM.de",font_size="20sp",color=(1,1,1,1))
proglabel = Label(text="None\nDeveloper",color=(1,1,1,0),font_size="13sp")
#proglabel.pos_hint_x = .2
#proglabel.pos_hint_y = 0
proglabel.pos_hint = {"x":.25,"y":-.4}
progimg = Image(source="loadingmat.gif",keep_ratio=False,allow_stretch=True,anim_delay=0.05)
progimg.size_hint = .14,.75
progimg.pos_hint ={"x":1.1,"y":.1}
progbg = RootWidget()
progbg.setbg(progbg,(1,1,1,1))
progbg.size_hinz = .15, 1
progbg.pos_hint = {"x":.85,"y":0}
titlebar.add_widget(progbg)
titlebar.add_widget(progimg)
titlebar.add_widget(proglabel)
titlelab.pos_hint = {"x":-.1,"y":0}
titlescat = ScatterLayout()
titlescat.size_hint = None,None
sidebar = RootWidget()
sidebar.setbg(sidebar,(.8,.8,.8,1))
sidebar.size_hint = .8,.9
sidebar.pos_hint = {"x":-.8,"y":0}
exitbt = Button(text="Beenden",background_color=(0,1,1,1))
exitbt.size_hint = 1,.1
exitbt.pos_hint = {"x":0,"y":0}
exitbt.bind(on_release=exitapp)
sidebar.add_widget(exitbt)
sidetitle = Label(text="Optionen",font_size="25sp",color=(0,0,0,1))
sidetitle.pos_hint = {"x":0,"y":.4}
sidebar.add_widget(sidetitle)
titlescat.size = 48,48
titlescat.pos_hint = {"x":0.025,"y":.25}
mencanv = RootWidget()
mencanv.size_hint= .1,.6
mencanv.pos_hint = {"x":0.025,"y":.2}
#titlebar.add_widget(mencanv)
titlebar.add_widget(titlescat)
titleflow = Button(background_normal="school.png",background_down="school.png")
titleflow.size_hint = None,None
titleflow.size = 48,48
titleflow.pos_hint = {"x":0,"y":0}
titleflow.bind(on_release=openmen)
titlescat.add_widget(titleflow)
titlebar.add_widget(titlelab)
mainscreen.add_widget(titlebar)
sm.add_widget(mainscreen)
sm.current = "logonscreen"

logo = Image(source="school.png")
#mainscreen.add_widget(logo)
mainscreen.add_widget(sidebar)


class MainApp(App):
    
    def build(self):
        global sm
        sleep(1,goto_start)
        return sm

if __name__ == "__main__":
    MainApp().run()