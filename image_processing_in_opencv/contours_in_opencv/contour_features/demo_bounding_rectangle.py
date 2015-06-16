# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate bounding rectangle (straight and rotated)
@author: Johnny
"""

import cv2
import numpy as np

img = cv2.imread('blue_thunder.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# Straight bounding rectangle
x, y, w, h = cv2.boundingRect(cnt)
img_bound_s = img.copy()
img_bound_s = cv2.rectangle(img_bound_s, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Rotated bounding rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img_bound_r = img.copy()
img_bound_r = cv2.drawContours(img_bound_r, [box], 0, (0, 0, 255), 2)

# Display all
cv2.imshow("Original", img)
cv2.imshow("Straight Bounding Rectangle", img_bound_s)
cv2.imshow("Rotated Bounding Rectangle", img_bound_r)
cv2.waitKey()
cv2.destroyAllWindows()
