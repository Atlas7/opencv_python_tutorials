# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:18:17 2015

@author: Johnny
"""
import cv2

img1 = cv2.imread('messi.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t