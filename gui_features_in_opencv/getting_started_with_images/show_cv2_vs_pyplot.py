# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:09:22 2015

@author: Johnny

Inspired by a Python code by user "Abid Rahman Kat" at this Stackoverflow forum
http://stackoverflow.com/questions/15072736/extracting-a-region-from-an-image-using-slicing-in-python-opencv/15074748#15074748

It demonstrates the difference between plotting with cv2 versus matplotlib.

cv2: bgr (true color); rgb (distorted color)

matplotlib: bgr (distorted color); rgb (true color)
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg')

# A quick way to flip bgr to rgb
img2 = img[:,:,::-1]

# view matplotlib subplot under IPython Console
plt.subplot(121);plt.title('PyPlot: bgr');plt.imshow(img) # bgr: expects distorted color
plt.subplot(122);plt.title('PyPlot: rgb');plt.imshow(img2) # rgb: expect true color
plt.show()

# view cv2 plots in separate windows
cv2.imshow('cv2: bgr image',img) # expects true color
cv2.imshow('cv2: rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()