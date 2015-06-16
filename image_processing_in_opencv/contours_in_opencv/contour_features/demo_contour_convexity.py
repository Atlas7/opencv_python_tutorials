# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate contouring an image with Hull Convexity.
@author: Johnny
"""

import cv2
import numpy as np

img = cv2.imread('blue2.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
hull = cv2.convexHull(cnt)

# check hull convexity
k = cv2.isContourConvex(hull)
print k

# Create the hull contour image
img_blank = np.zeros(img.shape, np.uint8)
img_hull = img_blank.copy()
cv2.drawContours(img_hull, hull, -1, (0, 0, 255), 3)  # plot points
cv2.drawContours(img_hull, [hull], 0, (0, 255, 0), 1)  # draw line

# Overlay hull contour on original image
img_unified = img.copy()
cv2.drawContours(img_unified, hull, -1, (0, 0, 255), 3)
cv2.drawContours(img_unified, [hull], 0, (0, 255, 0), 1)

# Display all
cv2.imshow("img", img)
cv2.imshow("img_hull", img_hull)
cv2.imshow("img_unified", img_unified)
cv2.waitKey()
cv2.destroyAllWindows()
