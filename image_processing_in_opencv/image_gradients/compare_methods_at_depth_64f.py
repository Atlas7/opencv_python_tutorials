# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:55:09 2015

@author: Johnny
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('box.png',0)

# Detect slopes in x and y directions with cv2.Laplacian with depth cv2.CV_64F and convert back to cv2.CV_8U
laplacian64f = cv2.Laplacian(img,cv2.CV_64F)
abs_laplacian64f = np.absolute(laplacian64f)
laplacian64f_8u = np.uint8(abs_laplacian64f)

# Detect slopes in x direction with cv2.Laplacian with depth cv2.CV_64F and convert back to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobelx64f = np.absolute(sobelx64f)
sobelx64f_8u = np.uint8(abs_sobelx64f)

# Detect slopes in y direction with cv2.Laplacian with depth cv2.CV_64F and convert back to cv2.CV_8U
sobely64f = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
abs_sobely64f = np.absolute(sobely64f)
sobely64f_8u = np.uint8(abs_sobely64f)

# Plot to show comparisons
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original\n(img)'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian64f_8u,cmap = 'gray')
plt.title('Laplacian\n(laplacian64f_8u)'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx64f_8u,cmap = 'gray')
plt.title('Sobel-x\n(sobelx64f_8u)'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely64f_8u,cmap = 'gray')
plt.title('Sobel-y\n(sobely64f_8u)'), plt.xticks([]), plt.yticks([])

plt.show()