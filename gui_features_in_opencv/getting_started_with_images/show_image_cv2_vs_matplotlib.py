# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:09:22 2015

@author: Johnny

A Python code by user "Abid Rahman Kat" at this Stackoverflow forum
http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748

It demonstrates the difference between plotting with cv2 (bgr) versus matplotlib (rgb).

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi_med.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()