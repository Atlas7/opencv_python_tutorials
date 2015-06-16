# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate Minimum Enclosing Circle.
@author: Johnny
"""

import cv2
import numpy as np


img = cv2.imread('blue_thunder.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# Minimum Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img_circle = img.copy()
img_circle = cv2.circle(img_circle, center, radius, (0, 255, 0), 2)

# Display all
cv2.imshow("Original", img)
cv2.imshow("Minimum Enclosing Circle", img_circle)
cv2.waitKey()
cv2.destroyAllWindows()
