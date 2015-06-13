# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015
Enhance the tutorial contour approximation example by adding trackbars to make experiments easier.
Try playing around with "factor" - the smaller the more accurate (and costly).
@author: Johnny
"""


import cv2
import numpy as np

# this function is needed for the createTrackbar step downstream
def nothing(x):
    pass

# Read image
img = cv2.imread('blue7.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Prepare a blank canvas to draw on...
img_blank = np.zeros(img.shape, np.uint8)

# Control panel
control_panel = "Control";
cv2.namedWindow(control_panel)

# add epsilon_factor trackbar to control panel
sliding_eps_factor = 'Epsilon Factor'
eps_scaling = 1000
cv2.createTrackbar(sliding_eps_factor, control_panel, 100, eps_scaling, nothing)

# add this dummy image to control panel so it become wider
img_control = np.zeros((20, 300), np.uint8)

# Infinite loop until we hit the escape key on keyboard
while(1):

    # get current positions of the trackbars
    value_eps_factor = cv2.getTrackbarPos(sliding_eps_factor, control_panel)
    
    # apply threshold and create a mask (img_thresh will get overwritten downstream)
    ret, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)
    img_mask = img_thresh.copy()
    
    # identify contours
    image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]  #  This program only picks out the first contour (a limitation)
    perimeter = cv2.arcLength(cnt, True)    
    factor = (value_eps_factor * 1.) / (eps_scaling * 1.)
    epsilon = factor * perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    # Draw all contour points only
    img_approx_points = img_blank.copy()
    cv2.drawContours(img_approx_points, approx, -1, (0, 0, 255), 3)
    
    # Draw the first contour line only (There is only one for this example)
    img_approx_line = img_blank.copy()
    cv2.drawContours(img_approx_line, [approx], 0, (0, 255, 0), 1)
    
    # Display a unified picture
    img_unified = img.copy()
    cv2.drawContours(img_unified, [approx], 0, (0, 255, 0), 1)  # line
    cv2.drawContours(img_unified, approx, -1, (0, 0, 255), 3)  # points
      
    # Display in windows...
    cv2.imshow(control_panel, img_control)
    cv2.imshow("img", img)
    cv2.imshow("img_gray", img_gray)
    cv2.imshow("img_mask", img_mask)
    cv2.imshow("img_approx_points", img_approx_points)
    cv2.imshow("img_approx_line", img_approx_line)
    cv2.imshow("img_unified", img_unified)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()
