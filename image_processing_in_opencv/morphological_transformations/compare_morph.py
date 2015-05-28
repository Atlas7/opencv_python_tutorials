# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:02:38 2015
Use this code to compare the effect of various morphological transformations.
For this exercise we use a 5-by-5 kernal by can be anything.
Inspred by OpenCV-Python Tutorials - Morphological Transformations
https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html#morphological-ops
@author: Johnny
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# numpy kernal creation method: 
# kernel = np.ones((5, 5), np.uint8)
# cv2 kernal creation method:
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# Note: the input is a grayscale image
img = cv2.imread('smily_original_noisy.png', 0)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

titles = [
    'original\n(think white soil)', 'erosion\n(losing soil)',
    'dilation\n(gaining soil)', 'gradient\n(dilation - erosion)',
    'opening\n(erode -> dilate)', 'closing\n(dilate -> erode)',
    'tophat\n(original - opening)', 'blackhat\n(original - closing)']

images = [img, erosion, dilation, gradient,
          opening, closing, tophat, blackhat]

for i in xrange(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
