# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate fitting an eclipse to a shape. Essentially a rotated rectangle (but eclipse shape).
@author: Johnny
"""

import cv2
import numpy as np


img = cv2.imread('blue_thunder.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# Fit a rotated eclipse
ellipse = cv2.fitEllipse(cnt)
img_eclipse = img.copy()
img_eclipse = cv2.ellipse(img_eclipse, ellipse, (0, 255, 0), 2)

# Display all
cv2.imshow("Original", img)
cv2.imshow("Fit an eclipse", img_eclipse)
cv2.waitKey()
cv2.destroyAllWindows()
