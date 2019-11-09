# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:28:11 2019

@author: Andrew 闫泽锋
"""
from gtts import gTTS
import os
def main():
    t = 'Shalom is so fattttt'
    language = 'en'
    myobj= gTTS(text=t, lang=language, slow=False) 
    
    myobj.save("audiotemp.mp3")
    os.system("audiotemp.mp3")
    
if __name__== "__main__":
    main()