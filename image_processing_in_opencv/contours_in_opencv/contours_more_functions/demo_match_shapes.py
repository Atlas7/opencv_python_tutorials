# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

img1 = cv2.imread('blue6.png', 0)
img2 = cv2.imread('blue6_rotated.png', 0)
img3 = cv2.imread('blue5.png', 0)

ret1, thresh1 = cv2.threshold(img1, 50, 255, 0)
ret2, thresh2 = cv2.threshold(img2, 50, 255, 0)
ret3, thresh3 = cv2.threshold(img3, 50, 255, 0)

image1, contours1, hierarchy1 = cv2.findContours(thresh1, 2, 1)
image2, contours2, hierarchy2 = cv2.findContours(thresh2, 2, 1)
image3, contours3, hierarchy3 = cv2.findContours(thresh3, 2, 1)

cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]

ret_1_1 = cv2.matchShapes(cnt1, cnt1, 1, 0.0)
ret_1_2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
ret_1_3 = cv2.matchShapes(cnt1, cnt3, 1, 0.0)


print "Match Shape Hu Moment Values"
print "img1 vs img1: " + str(ret_1_1)
print "img1 vs img2: " + str(ret_1_2)
print "img1 vs img3: " + str(ret_1_3)
