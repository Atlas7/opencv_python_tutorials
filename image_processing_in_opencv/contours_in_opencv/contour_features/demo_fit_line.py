# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Illustrate fitting a line to a shape.
@author: Johnny
"""

import cv2
import numpy as np


img = cv2.imread('blue_thunder.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# Fit a line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img_line = img.copy()
img_line = cv2.line(img_line, (cols-1, righty), (0, lefty), (0, 255, 0), 2)

# Display all
cv2.imshow("Original", img)
cv2.imshow("Fit a line", img_line)
cv2.waitKey()
cv2.destroyAllWindows()
