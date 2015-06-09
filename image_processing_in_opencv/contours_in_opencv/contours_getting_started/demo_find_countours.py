# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 17:48:34 2015

@author: Johnny

Illustrate the tutorial contour demo.
"""

import numpy as np
import cv2


img = cv2.imread('tom_cruise.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 170, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_with_contours = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
cv2.imshow("image", image)
cv2.imshow("img", img)
cv2.waitKey()
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
