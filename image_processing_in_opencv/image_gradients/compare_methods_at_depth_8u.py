# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:55:09 2015

@author: Johnny
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('davemark_sudoku.jpg', 0)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
scharrx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=-1)
scharry = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=-1)

titles = [
    'Original\n(img)', 'Sobel-x\n(sobelx)', 'Scharr-x\n(scharrx)',
    'Laplacian\n(laplacian)', 'Sobel-y\n(sobely)', 'Scharr-y\n(scharry)']

images = [img, sobelx, scharrx,
          laplacian, sobely, scharry]

for i in xrange(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
