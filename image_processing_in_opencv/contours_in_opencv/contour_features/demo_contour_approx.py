# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate a simple contour approximation example.
Try playing around with "factor" - the smaller the more accurate (and costly).
(whilst keeping "threshold" constant)
@author: Johnny
"""


import cv2
import numpy as np

img = cv2.imread('blue0.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold = 50  # Adjust this if neccessary
ret, img_thresh = cv2.threshold(img_gray, threshold, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]  #  note that in this example there is only one contour
perimeter = cv2.arcLength(cnt, True)

# configure approx factor (with repect to perimeter) - the lower, the more accurate
factor = 0.001  # vary this to see the effect (the smaller the more accurate but costly)
epsilon = factor*perimeter
approx = cv2.approxPolyDP(cnt, epsilon, True)

# Prepare a blank canvas to draw on...
img_blank = np.zeros(img.shape, np.uint8)

# Draw all contour points only
img_approx_points = img_blank.copy()
cv2.drawContours(img_approx_points, approx, -1, (0, 0, 255), 3)

# Draw the first contour line only (There is only one for this example)
img_approx_line = img_blank.copy()
cv2.drawContours(img_approx_line, [approx], 0, (0, 255, 0), 1)

# Display a unified picture
img_unified = img.copy()  # original
cv2.drawContours(img_unified, [approx], 0, (0, 255, 0), 1)  # line
cv2.drawContours(img_unified, approx, -1, (0, 0, 255), 3)  # points

# Display in windows...
cv2.imshow("img", img)
cv2.imshow("img_gray", img_gray)
cv2.imshow("img_thresh", img_thresh)
cv2.imshow("img_approx_points", img_approx_points)
cv2.imshow("img_approx_line", img_approx_line)
cv2.imshow("img_unified", img_unified)
cv2.waitKey()
cv2.destroyAllWindows()
