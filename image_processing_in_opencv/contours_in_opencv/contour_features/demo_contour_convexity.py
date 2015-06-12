# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015

@author: Johnny
"""

import cv2
import numpy as np

img = cv2.imread('hand.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
hull = cv2.convexHull(cnt)

# Display the hull contour points
img_hull = np.zeros(img.shape, np.uint8)
cv2.drawContours(img_hull, hull, -1, (0, 255, 0), 2)
cv2.imshow("img", img)
cv2.imshow("img_hull", img_hull)
cv2.waitKey()
cv2.destroyAllWindows()