# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:20:05 2015
Illustrate Perspective Transformation of an image.
@author: Johnny
"""
#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

#%%
img_bgr = cv2.imread('messi.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB);
rows,cols,ch = img_rgb.shape
print "(x, y) : " + str((cols, rows))

#%%
# Map 4 points (quadrangle vertices) from space 1 to space 2 (think JotNot)
pts1 = np.float32([[95, 88],[381, 5],[189, 472],[669, 460]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst_rgb = cv2.warpPerspective(img_rgb,M,(300,300))

#%%
plt.subplot(121),plt.imshow(img_rgb),plt.title('Input')
plt.subplot(122),plt.imshow(dst_rgb),plt.title('Output')
plt.show()