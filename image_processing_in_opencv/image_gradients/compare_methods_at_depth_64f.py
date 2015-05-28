# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:55:09 2015

@author: Johnny
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('davemark_sudoku.jpg',0)

# Detect slopes in x and y directions with cv2.Laplacian with depth cv2.CV_64F and convert back to cv2.CV_8U
laplacian64f = cv2.Laplacian(img,cv2.CV_64F)
abs_laplacian64f = np.absolute(laplacian64f)
laplacian64f_8u = np.uint8(abs_laplacian64f)

# Detect slopes in x direction with cv2.Sobel with depth cv2.CV_64F and convert back to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
abs_sobelx64f = np.absolute(sobelx64f)
sobelx64f_8u = np.uint8(abs_sobelx64f)

# Detect slopes in y direction with cv2.Sobel with depth cv2.CV_64F and convert back to cv2.CV_8U
sobely64f = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
abs_sobely64f = np.absolute(sobely64f)
sobely64f_8u = np.uint8(abs_sobely64f)

# Detect slopes in x direction with cv2.Scharr with depth cv2.CV_64F and convert back to cv2.CV_8U
scharrx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=-1)
abs_scharrx64f = np.absolute(scharrx64f)
scharrlx64f_8u = np.uint8(abs_scharrx64f)

# Detect slopes in y direction with cv2.Scharr with depth cv2.CV_64F and convert back to cv2.CV_8U
scharry64f = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=-1)
abs_scharry64f = np.absolute(scharry64f)
scharry64f_8u = np.uint8(abs_scharry64f)

titles = [
    'Original\n(img)', 'Sobel-x\n(sobelx64f_8u)', 'Scharr-x\n(scharrx64f_8u)',
    'Laplacian\n(laplacian64f_8u)', 'Sobel-y\n(sobely64f_8u)', 'Scharr-y\n(scharry64f_8u)',]
     

images = [img, sobelx64f_8u, scharrlx64f_8u,
          laplacian64f_8u, sobely64f_8u, scharry64f_8u]

for i in xrange(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()