
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
import os
menopen = False

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
    global titleflow, menopen
    if menopen == True:
        closemen()
        menopen = False
        return 0
    menopen = True
    am = Animation(rotation=180,t="in_quad",duration=.2,step=1.0/180.0)
    am.start(titlescat)
def closemen():
    global titleflow
    am = Animation(rotation=0,t="in_quad",duration=.2)
    am.start(titlescat)
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
titlelab = Label(text="SCHOLLGYM.de",font_size="20sp",color=(1,1,1,1))
titlelab.pos_hint = {"x":0,"y":0}
titlescat = ScatterLayout()
titlescat.size_hint = None,None
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
mainscreen.add_widget(logo)


class MainApp(App):
    
    def build(self):
        global sm
        sleep(1,goto_start)
        return sm

if __name__ == "__main__":
    MainApp().run()