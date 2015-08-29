







LICENSE = """Lizenz
============

Fuer die Nutzung dieser App musst du diesen Bedingungen zustimmen:

1. Garantie
Es wird nicht garantiert, dass die in dieser App angegebenen Daten korrekt oder
vollstaendig sind. ASapplications uebernimmt keine Haftung fuer jegliche Fehler.
Die Wahrscheinlichkeit einer Fehlinformation steigt, wenn sie keine aktuelle Version der App auf ihrem Mobiltelefon installiert haben.

2. Veraenderungen der App
Obgleich diese App kostenlos ist, ist es verboten diese App ohne Genehmigung von ASapplications zu verbreiten.

3. Angaben der Nutzer
Die Angaben der Nutzer werden unverschluesselt auf einem oeffentlichem FTP - Server gespeichert. Nutzen sie deshalb andere Passwoerter als bei anderen Accounts. Mit der Nutzung erklaeren sie sich mit der unverschluesselten Datenspeicherung einverstanden.

4. Netzwerkverkehr
Diese App laedt Vertrerungsdaten ueber das Internet herunter. Fuer anfallende Kosten der Mobilfunkbetreiber uebernimmt ASapplications keine Haftung.

5. Infos zu Services
Solange das App - Symbol in der Statusleiste vorhanden ist, werden sie bei bestehender Internetverbindung automatisch ueber Aenderungen informiert.

Der Eigentuemer dieser App ist ASapplications (R)
"""

from kivy.app import App
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout
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
from lxml import etree
import HTMLParser
import zipfile
import sys
import re
import os
import lxml.html
import ftplib
import threading
import time
import urllib
#VPWEBSITE = "http://planung.schollgym.de/plaene/Anzeige-Homepage/Schueler-morgen/subst_001.htm"
NEWSSITE = "https://schollgym.lima-city.de/appdata/updates.html"
VPWEBSITE = " http://vertretung.lornsenschule.de/schueler/f1/subst_001.htm"
MAINWEBSITE = "http://www.schollgym.de"
ZOOMWEBSITE = "http://zeitung.schollgym.de"
threads = []
menopen = False
inprogress = False
platform = "android"


class dummys:
    def toast(msg):
        pass

def toast_android(msg):
    PythonActivity.toastError(msg)


if sys.platform == "win32":
    print("USING WINDOWS PLATFORM. ABORTING ANDROID STUFF")
    toast = dummys.toast
else:
    from jnius import autoclass
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    toast = toast_ansdroid





nums = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate(KEY=""):
    Window.rotation = 270



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
def store(name,text):
    f = open("tmp","w")
    f.write(text)
    f.close()
    file = open("tmp","r")
    server.storbinary("STOR "+name,file)
    file.close()
    os.remove("tmp")




def startftp(KEY=""):
    global server
    #printd("[FTP] Connecting to server...")
    server = ftplib.FTP("ftp.lima-city.de")
    #printd("[FTP] logging in to server...")
    server.login("schollgym","SchollGym15")




def log(msg,timestamp=True):
    f = open("/sdcard/.schollgymde/log","a")
    if timestamp:
        f.write(str(time.strftime("%Y/%m/%d$%H:%M:%S")) + " > " + msg + "\n")
    else:
        f.write(msg+"\n")
    f.close()



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


log("\n",False)
log("Started Schollgym.de")



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
    log("Fetching Data")
    #speedtest
    try:
        start = time.clock()
        urllib.urlretrieve(VPWEBSITE,"/sdcard/.schollgymde/vp")
        end = time.clock()
        if end - start < 2:
            notshowp = True
    except:
         startprog("Offline")
         log("Offline: Not fetched "+str(VPWEBSITE))
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
         log("Offline: Not fetched "+str(VPWEBSITE))
         sleep(2,stopprog)
         return 0
    if not notshowp:
        startprog("Lade\nHauptseite")
    try:
        urllib.urlretrieve(MAINWEBSITE,"/sdcard/.schollgymde/website")
    except:
        startprog("Offline")
        log("Offline: Not fetched "+str(MAINWEBSITE))
        sleep(2,stopprog)
        return 0
    if not notshowp:
        startprog("Lade\nZeitungsartikel")
    try:
        urllib.urlretrieve(ZOOMWEBSITE,"/sdcard/.schollgymde/newspaper")
    except:
         startprog("Offline")
         log("Offline: Not fetched "+str(ZOOMWEBSITE))
         sleep(2,stopprog)
         return 0
    if not notshowp:
        startprog("Lade\nNews")
    try:
        urllib.urlretrieve(NEWSSITE,"/sdcard/.schollgymde/news")
    except:
        startprog("Offline")
        log("Offline: Not fetched "+str(NEWSSITE))
        sleep(2,stopprog)
        return 0
    stopprog()
def parse():
    vpfile = open("/sdcard/.schollgymde/vp","r")
    vpt = vpfile.read().replace("\\n","\n")
    p = TableParser()
    p.feed(vpt)
    parsed = p.getres()
    log(str(p.getres()))
    parts = []
    formyclass = False
    subjcntr = 0
    nowsubj = []
    endsubj = 6
    for subj in parsed:
        if subj == CLASS:
            # Subjects for the class
            formyclass = True
            continue
        elif len(subj) < 4:
           if len(subj) == 1:
              subj2 = subj
              subj = "x"
           if subj[0] in nums:
            if subj[1] in nums:
               if len(subj) == 3:
                if subj[2] in alphabet:
                   # Muster: 10a NumNumLetter
                   # => not searched class but another
                   formyclass = False
                   continue
            elif subj[1] in alphabet:
                   # Muster: 5b NumLetter
                   # => Not searched
                   formyclass = False
                   continue
        if subj == "x":
              subj = subj2
        if formyclass:
         subjcntr += 1
         nowsubj.append(subj)
         if subjcntr == endsubj:
                  parts.append(nowsubj)
                  nowsubj = []
                  subjcntr = 0
    log(str(parts))
    fillvp(parts)



def fillvp(l):
    global vpinf
    if len(l) != 0:
        vpinf.text = "" #remove no vp message
    for item in l:
         # one item is one part of vp
         vpinf.text = vpinf.text + item[0] + ". Std: "+item[1] + ": "+item[2]+"\n"
    #readnews()

class TableParser(HTMLParser.HTMLParser):
     def __init__(self):
         HTMLParser.HTMLParser.__init__(self)
         self.endresult = []
         self.in_td = False
         self.in_div = False
     
     def handle_starttag(self, tag, attrs):
         if tag == 'td':
             self.in_td = True
         if tag == 'div':
             #print "hallo div"
             self.in_div = True
     
     def handle_data(self, data):
         global dayt
         if self.in_td:
             #print data
             self.endresult.append(data)
         if self.in_div:
             dayt = data
     
     def handle_endtag(self, tag):
         self.in_td = False
         self.in_div = False
     def getres(self):
         return self.endresult


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
    sleep(1,readnews)
    inprogress = False
    am = Animation(duration=.5,pos_hint={"x":.25,"y":-.4},color=(1,1,1,0),t="in_quad")
    am.start(proglabel)
    am2 = Animation(duration=.5,pos_hint={"x":1.2,"y":0},t="in_quad")
    am2.start(progimg)
def openvp(KEY=""):
    global vpframe,vpopenbt,vpisopen, vpinf
    if vpisopen:
        am = Animation(duration=1,pos_hint={"x":1,"y":1},t="in_out_circ")
        am2 = Animation(duration=1,pos_hint={"x":.85,"y":.78},t="in_out_circ")
        am.start(vpframe)
        am2.start(vpopenbt)
        vpisopen = False
        return 0

    vpisopen = True
    if os.path.isfile("/sdcard/.schollgymde/vp"):
        try:
            parse()
        except Exception, e:
            vpinf.text = "Error while parsing\nContent:\n"+str(e)
    am = Animation(duration=1,pos_hint={"x":.3,"y":.3},t="in_out_circ")
    am2 = Animation(duration=1,pos_hint={"x":.15,"y":.18},t="in_out_circ")
    am.start(vpframe)
    am2.start(vpopenbt)



def acceptlic(KEY=""):
    global sm
    sm.current = "licscreen"
def licok(KEY=""):
    file = open("/sdcard/.schollgymde/licac","w")
    file.write("Accepted")
    file.close()
    if os.path.isfile("/sdcard/.schollgymde/sets"):
            sleep(1,goto_start)
    else:
             sm.add_widget(settingss)
             sm.current = "settings"
    #sleep(1,goto_start)
def licnok(key=""):
    exit()


def savesets(KEY=""):
    global sm
    startftp()
    usr = usrnorm = clone("/usr/index","r")
    usr = usr.split("\n")
    foundname = False
    for name in usr:
        if name == setname.text+":"+setname2.text:
            foundname = True
    if foundname:
        toast("Name schon vergeben")
        return 0
    store("/usr/index",usrnorm+setname.text+":"+setname2.text+"\n")
    server.mkd("/usr/"+setname.text+setname2.text)
    sdata("usrname",setname.text)
    sdata("usrname2",setname2.text)
    file = open("/sdcard/.schollgymde/sets","w")
    file.write(setclass.text)
    file.close()
    goto_start()


def data(name,notfound=False):
    if os.path.isfile("/sdcard/.schollgymde/"+name) == False:
        return notfound
    f = open("/sdcard/.schollgymde/"+name,"r")
    t = f.read()
    f.close()
    return t



def sdata(name,content):
    f = open("/sdcard/.schollgymde/"+name,"w")
    f.write(content)
    f.close()



def goto_secure(KEY=""):
    global sm
    rotate()
    sm.transition = NoTransition()
    sm.current = "secac"

def writets():
    global tstowrite, term
    for letter in tstowrite:
        term.text += letter
        time.sleep(tstowait)
def ts(text,wait=0.01):
    global sm, term, tstowrite, tstowait
    tstowait = wait
    tstowrite = text
    threading.Thread(target=writets).start()
    return len(text)*wait




def acdata(name,notfound=False):
    try:
        t = clone("/usr/"+usrid+"/"+name,"r")
        return t
    except:
        return notfound


def sacdata(name,content):
    store("/usr/"+usrid+"/"+name,content)

    




def showdeny():
    global secac, denyframe
    for i in range(2):
        secac.add_widget(denyframe)
        time.sleep(.5)
        secac.remove_widget(denyframe)
        time.sleep(.5)
    secac.add_widget(denyframe)
    time.sleep(1.5)
    secac.remove_widget(denyframe)

def ts2(text,wait=0):
    global term
    term.text += text


def firecmd(cmd):
    global sm, usrid, oldusrid
    oldusrid = usrid
    HELP = "\nhelp - Print this help\nlogout - Log out from the ADSAC\nexit - Exit the app\nusr [user id] - Set the current working account\nregister [name] [content: optional]\ncat [name]"
    if cmd == "logout":
        term.text = ""
        termin.text = "COMMAND INPUT"
        sm.current = "mainscreen"
    elif cmd == "help":
        ts2(HELP+"\n",0.00)
    elif cmd == "exit":
        exitapp()
    elif re.search("^usr ",cmd):
        usrid = cmd.replace("usr ","")
    elif re.search("^register ",cmd):
        cmd = cmd.split(" ")
        if len(cmd) < 2:
            ts2("Not enough arguments. Min. 1 expected\n",0.00)
            return 0
        if len(cmd) == 2:
            cmd.append("")
        sacdata(cmd[1],cmd[2])
    elif re.search("^cat ",cmd):
        cmd = cmd.split(" ")
        t = acdata(cmd[1])
        if t == False:
            ts2("IOError: No such file or directory\n",0.00)
        else:
            ts2("Content of specified file:\n-----------------------------\n"+str(t),0.00)
        

    ts2("ADSAC $ ",0.00)

def termcmd(KEY=""):
    cmd = termin.text
    termin.text = ""
    #towait = ts(cmd+"\n")
    term.text += cmd + "\n"
    #sleep(towait,lambda KEY: firecmd(cmd))
    firecmd(cmd)


def wronglogin(KEY=""):
    global sm
    sm.current = "secac"
    threading.Thread(target=showdeny).start()



def usrlogin(KEY=""):
    global usrid
    oldusrid = usrid
    usrid = secname.text+secpwd.text
    if acdata("dev") == False:
        sleep(1,wronglogin)
        usrid = oldusrid
        return 0
    usrid = oldusrid
    ts("\n\nWaiting for your commands\n\nFTP Server: / , local: ~  $")


def cmdftp(KEY=""):
    try:
       startftp()
       ts("\nServer connection: OK\n")
       sleep(2.5,usrlogin)
       #sleep(2.5,wronglogin)
    except Exception as e:
        ts("\nERROR: "+str(e)+"\n")
        sleep(5,wronglogin)

def termlogon(KEY=""):
    global sm
    # server things
    sm.transition = NoTransition()
    sm.current = "termscreen"
    ts("ASapplications Development Security Access Console ADSAC\nThis place is absolutely secure and blocked for all normal users.\nChecking User Credentials...")
    sleep(4,cmdftp)
    #sleep(5,wronglogin)




def readnews(KEY=""):
    global mainscroll, newsblocks, news, mainblock
    print("========================== READING NEWS ==============================")
    if os.path.isfile("/sdcard/.schollgymde/news") == False:
        print("NO NEWS")
        return 0
    news = []
    file = open("/sdcard/.schollgymde/news","r")
    for line in file:
        line = line[:-1]
        if re.search("^//",line):
            continue
        if line == "":
            continue
        line = line.split("::")
        news.append([line[0],line[1].replace("\\n","\n")])
    print(news)
    newscntr = 0
    count = False
    if len(news) > 5:
        count = True
    for new in news:
        newsblocks[newscntr] = RootWidget()
        newsblocks[newscntr].setbg(newsblocks[newscntr],(.98,.98,.98,1))
        headline = Label(text=new[0],pos_hint={"x":0,"y":.4},color=(0,0,0,1))
        top = .2
        if len(new[1].split("\n")) > 1:
            for i in range(len(new[1].split("\n"))):
                top = top - .1
        content = Label(text=new[1],markup=True,pos_hint={"x":0,"y":.2},halign="center",shorten=True,color=(0,0,0,1))
        newsblocks[newscntr].add_widget(headline)
        newsblocks[newscntr].add_widget(content)
        mainblock.add_widget(newsblocks[newscntr])
        newscntr += 1
        if count:
            if newscntr > 6:
                mainblock.size_hint = (1, float(mainblock.size_hint[1])+0.2)
    



vpisopen = False
winsize = (Window.width,Window.height)
sm = ScreenManagerExtended()




#news = [["SCHOLL","Gymnasium fuehrt App ein"],["JO","JO IST COOL"],["BLA","BLA CAR"],["1","1"],["2","2"],["3","3"],["4","4"]]
#for i in range(30):
#    news.append(["6","6"])

mainscroll = ScrollView(size_hint=(.9,.9),pos_hint={"x":.05,"y":0})
mainblock = GridLayout(size_hint=(1,1),spacing=3,pos_hint={"x":0,"y":0},cols=1)
mainscroll.add_widget(mainblock)
newsblocks = {}
#readnews()



denyframe = RootWidget()
denyframe.setbg(denyframe,(.2,0,0,1))
denyframe.add_widget(Label(text="! Access Denied !",color=(.9,0,0,1),font_size="40sp",pos_hint={"x":0,"y":0}))
denyframe.size_hint = .5,.13
denyframe.pos_hint = {"x":.25,"y":.5}



terms = NewScreen(name="termscreen")
term = TextInput(background_normal="",text="",background_color=(0,0,0,1),foreground_color=(0,.8,0,1),size_hint=(1,.92),pos_hint={"x":0,"y":.08})
terms.add_widget(term)
termin = TextInput(background_normal="",text="COMMAND INPUT",background_color=(0,0,0,1),foreground_color=(0,.8,0,1),size_hint=(1,.08),pos_hint={"x":0,"y":0},multiline=False)
terms.add_widget(termin)
termin.bind(on_text_validate=termcmd)
secac = NewScreen(name="secac")


seclog = Image(source="security.png")
seclog.size_hint = .4,.8
seclog.pos_hint = {"x":.05,"y":.1}

seclab = Label(text="ASapplications Security System Access\n\nYou are going to access the Security\nSystem now. This place is only opened\nfor verified Developers of ASapplications\nEnter your Credentials.",font_size="19sp",color=(0,0,.8,1))
seclab.pos_hint = {"x":.2,"y":.2}
secac.add_widget(seclab)

secgo = Button(text="Access",background_normal="",background_down="",background_color=(0,0,.9,1))
secgo.size_hint = .2,.08
secgo.pos_hint = {"x":.8,"y":.1}
secac.add_widget(secgo)
secgo.bind(on_release=termlogon)

secac.add_widget(seclog)

secname = TextInput(multiline=False,background_normal="",foreground_color=(1,1,1,1),text="Name",background_color=(0,0,.6,1))

secname.size_hint = .4, .08
secname.pos_hint = {"x":.6,"y":.4}
secac.add_widget(secname)

secpwd = TextInput(multiline=False,background_normal="",foreground_color=(1,1,1,1),text="123456",password=True,background_color=(0,0,.6,1))

secpwd.size_hint = .4, .08
secpwd.pos_hint = {"x":.6,"y":.3}
secac.add_widget(secpwd)


settingss = NewScreen(name="settings")
settingss.setbg(settingss,(1,1,1,1))

settitle = Label(text="Einstellungsassitent",font_size="20sp",color=(0,0,0,1),pos_hint={"x":0,"y":.45})
settingss.add_widget(settitle)

setclass = TextInput(text="Deine Klasse und Buchstabe (z.B. 8d)",multiline=False,size_hint=(.9,.1),pos_hint={"x":.05,"y":.8})
settingss.add_widget(setclass)

setname = TextInput(text="Vorname",multiline=False,pos_hint={"x":0,"y":.7},size_hint=(.5,.1))

setname2 = TextInput(text="Nachnahme (Nutze echte Angaben)",multiline=False,pos_hint={"x":.5,"y":.7},size_hint=(.5,.1))
settingss.add_widget(setname2)
settingss.add_widget(setname)

oksets = Button(text="Abspeichern",size_hint=(1,.1),pos_hint={"x":0,"y":0})
settingss.add_widget(oksets)

oksets.bind(on_release=savesets)






licscreen = NewScreen(name="licscreen")
licscreen.setbg(licscreen,(1,1,1,1))
liclabel = TextInput(background_color=(1,1,1,1),background="",font_size="11sp")
liclabel.size_hint = 1,.9
liclabel.pos_hint = {"x":0,"y":.1}
licscreen.add_widget(liclabel)
licyes = Button(text="Akzeptieren",size_hint=(.5,.1),pos_hint={"x":0,"y":0})
licscreen.add_widget(licyes)
licno = Button(text="Verweigern",size_hint=(.5,.1),pos_hint={"x":.5,"y":0})
licscreen.add_widget(licno)
licyes.bind(on_release=licok)
licno.bind(on_release=licnok)

liclabel.text = LICENSE

mainscreen = NewScreen(name="mainscreen")
mainscreen.setbg(mainscreen,(1,1,1,1))
mainscreen.add_widget(mainscroll)
logonscreen = NewScreen(name="logonscreen")
sc = Image(source="school_white.png")
sm.add_widget(logonscreen)
logonscreen.add_widget(sc)
titlebar = RootWidget()
titlebar.setbg(titlebar,(63.0/255.0,81.0/255.0,181.0/255.0,1))
titlebar.size_hint = 1, .1
titlebar.pos_hint = {"x":0,"y":0.9}
vpopenbt = Button(background_normal="bag.png",background_down="bag.png", pos_hint={"x":.85,"y":.78},size_hint=(.15,.12))
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
secbt = Button(text="Entwickler - Bereich",background_color=(0,0,0,1))
secbt.size_hint = 1,.1
secbt.pos_hint = {"x":0,"y":.8}
sm.add_widget(secac)
secbt.bind(on_release=goto_secure)
sidebar.add_widget(secbt)
sidetitle = Label(text="Optionen",font_size="25sp",color=(0,0,0,1))
sidetitle.pos_hint = {"x":0,"y":.45}
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
sm.add_widget(terms)
sm.current = "logonscreen"

logo = Image(source="school.png")
#mainscreen.add_widget(logo)
mainscreen.add_widget(sidebar)





us1 = data("usrname")
us2 = data("usrname2")

if us1:
    usrid = us1+us2





class MainApp(App):
    
    def build(self):
        global sm, CLASS
        if platform == 'android':
            if sys.platform != "win32":
                from android import AndroidService
                service = AndroidService('Vertretungsplan wird kontrolliert', 'Keine Benachrichtigung, Wenn Meldung weg ist.')
                service.start('service started')
                self.service = service
        if os.path.isfile("/sdcard/.schollgymde/licac"):
            if os.path.isfile("/sdcard/.schollgymde/sets"):
                clf = open( "/sdcard/.schollgymde/sets","r")
                CLASS = clf.read()
                clf.close()
                sleep(1,goto_start)
            else:
                sm.add_widget(settingss)
                sm.current = "settings"
        else:
            sm.add_widget(licscreen)
            sleep(1,acceptlic)
        return sm

if __name__ == "__main__":
    MainApp().run()
