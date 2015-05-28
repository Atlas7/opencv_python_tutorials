# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:07:44 2015
Illustrate these regarding the cv2.Sobel method:

- using depth cv2.CV_8U will pick on only positive slope (black to white),
  but not negative slope (white to black). 
  example: sobelx8u
  
- using higher order depth cv2.CV_64F, take absolte value, then convert back
  to cv2.CV_8U, will pick up both positive and negative slopes.
  example: sobelx64f_8u
  
@author: Johnny
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('box.png',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
abs_sobelx64f = np.absolute(sobelx64f)
sobelx64f_8u = np.uint8(abs_sobelx64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original\n(img)'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel-x\nDepth: cv2.CV_8U\n(sobelx8u)'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobelx64f_8u, cmap='gray')
plt.title('Sobel-x\nDepth: abs(cv2.CV_64F)\n(sobelx64f_8u)'), plt.xticks([]), plt.yticks([])
plt.show()
