# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:09:12 2019

@author: Andrew 闫泽锋
"""

import cv2
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import time
def getIm():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False
    
    img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   
#    plt.imshow(img1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.show()
    
    result = Image.fromarray(img1,'RGB')
    result.save('temp.jpg')
    
    cap.release()
    return result
def main():
    for i in range(15):
        time.sleep(5)
        x=getIm()
        im = Image.open('temp.jpg')
        
        im.show()
#    Image.open("temp.jpg")
    
if __name__== "__main__":
    main()