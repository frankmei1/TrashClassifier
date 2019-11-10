# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:28:11 2019

@author: Andrew
"""
from gtts import gTTS
import os
def playSound(str):
    #get file

    if str == "trash":
        t = 'Throw that away!!!!'
    else:
        t = 'Stop! recycle that please'
    language = 'en'
    myobj= gTTS(text=t, lang=language, slow=False)

    myobj.save("audiotemp.mp3")
    os.system("audiotemp.mp3")

playSound("trash")
