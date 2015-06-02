# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 21:31:17 2015
This is the basic Canny Edge Detection code supplied by the
original OpenCV-Python Tutorials.
@author: Johnny
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
