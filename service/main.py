from plyer import notification
from plyer import tts
from plyer.utils import platform
from plyer.compat import PY2
from plyer import vibrator

notification.notify(title="hallo",message="welt")

from lxml import etree
import HTMLParser
import zipfile
import sys
import os
import lxml.html
import threading
import time
import urllib
#VPWEBSITE = "http://planung.schollgym.de/plaene/Anzeige-Homepage/Schueler-morgen/subst_001.htm"
VPWEBSITE = "http://vertretung.lornsenschule.de/schueler/f1/subst_001.htm"
MAINWEBSITE = "http://www.schollgym.de"
ZOOMWEBSITE = "http://zeitung.schollgym.de"


CLASS = "05d"



def vpthread():
    global done
    notshowp = False
    try:
        urllib.urlretrieve(VPWEBSITE,"/sdcard/.schollgymde/vp")
    except:
         return 0
    try:
        urllib.urlretrieve(MAINWEBSITE,"/sdcard/.schollgymde/website")
    except:
        return 0
    try:
        urllib.urlretrieve(ZOOMWEBSITE,"/sdcard/.schollgymde/newspaper")
    except:
         return 0
    parse()


def parse():
    vpfile = open("/sdcard/.schollgymde/vp","r")
    vpt = vpfile.read().replace("\\n","\n")
    p = TableParser()
    p.feed(vpt)
    parsed = p.getres()
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
    fill(parts)



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



def fill(l):
    n = ""
    for item in l:
        n+= item[0]+". "+item[2]
    notification.notify(title="Neue Vertretung(en)",message=n)
    


while True:
    vpthread()
    time.sleep(30)

