# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:58:19 2015
Illustrate affine transformation of an image.
@author: Johnny
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('messi.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB);

rows,cols,ch = img_rgb.shape

# Map 3 points (triangle vertices) from space 1 to space 2.
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst_rgb = cv2.warpAffine(img_rgb,M,(cols,rows))

plt.subplot(121),plt.imshow(img_rgb),plt.title('Input')
plt.subplot(122),plt.imshow(dst_rgb),plt.title('Output')
plt.show()
