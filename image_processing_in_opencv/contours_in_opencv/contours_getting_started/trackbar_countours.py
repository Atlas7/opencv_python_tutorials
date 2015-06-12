# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 17:48:34 2015

@author: Johnny

An enhanced version of the original simple tutorial contour demo - added
trackbar to vary threshold - so we get to see contour lines at various
grayscale (between 0 and 255).
"""

import numpy as np
import cv2


# this function is needed for the createTrackbar step downstream
def nothing(x):
    pass

# read image
img = cv2.imread('tom_cruise.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

window_name = 'Contour Plotter'

# Initialize window to show
cv2.namedWindow(window_name)

# add ON/OFF switch to "contourer"
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, window_name, 0, 1, nothing)

# add threshold slidebar to "contourer"
th = 'Threshold'
cv2.createTrackbar(th, window_name, 0, 255, nothing)

# Infinite loop until we hit the escape key on keyboard
while(1):

    out_image = img.copy()
    # get current positions of the trackbars
    s = cv2.getTrackbarPos(switch, window_name)
    t = cv2.getTrackbarPos(th, window_name)

    # re-generate image based on trackbar values
    if s == 0:
        """ do nothing """
    else:
        """ re-plot contours """     
        ret, thresh = cv2.threshold(imgray, t, 255, cv2.THRESH_BINARY)
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        out_image = cv2.drawContours(out_image, contours, -1, (0, 255, 0), 1, CV_AA)

    cv2.imshow(window_name, out_image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()
