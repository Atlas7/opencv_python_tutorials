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
img = cv2.imread('plate.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Prepare a blank canvas to draw on...
img_blank = np.zeros(img.shape, np.uint8)

# Control panel
control_panel = "Control";
cv2.namedWindow(control_panel)

# add ON/OFF switch to the control trackbar
sliding_switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(sliding_switch, control_panel, 0, 1, nothing)

# add threshold trackbar to control panel
sliding_threshold = 'Threshold'
cv2.createTrackbar(sliding_threshold, control_panel, 50, 254, nothing)

# add epsilon_factor trackbar to control panel
sliding_eps_factor = 'Epsilon Factor'
eps_scaling = 1000
cv2.createTrackbar(sliding_eps_factor, control_panel, 100, eps_scaling, nothing)

# Infinite loop until we hit the escape key on keyboard
while(1):

    # get current positions of the trackbars
    value_switch = cv2.getTrackbarPos(sliding_switch, control_panel)
    value_threshold = cv2.getTrackbarPos(sliding_threshold, control_panel) 
    value_eps_factor = cv2.getTrackbarPos(sliding_eps_factor, control_panel) 
    
    # prepare blank canvases
    img_thresh = img_blank.copy()       
    img_approx_points = img_blank.copy()
    img_approx_line = img_blank.copy()
    img_unified = img.copy()  # original
    
    if value_switch == 0:
        """ do nothing """       
    else:       
        """ re-plot contours """      
        ret, img_thresh = cv2.threshold(img_gray, value_threshold, 255, cv2.THRESH_BINARY)
        image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]  #  note that in this example there is only one contour
        perimeter = cv2.arcLength(cnt, True)
        
        factor = (value_eps_factor*1.) / (eps_scaling*1.)
        epsilon = factor * perimeter
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        # Draw all contour points only        
        cv2.drawContours(img_approx_points, approx, -1, (0, 0, 255), 3)
        
        # Draw the first contour line only (There is only one for this example)
        cv2.drawContours(img_approx_line, [approx], 0, (0, 255, 0), 1)
        
        # Display a unified picture
        cv2.drawContours(img_unified, [approx], 0, (0, 255, 0), 1)  # line
        cv2.drawContours(img_unified, approx, -1, (0, 0, 255), 3)  # points
      
    # Display in windows...
    cv2.imshow("img", img)
    cv2.imshow("img_gray", img_gray)
    cv2.imshow("img_thresh", img_thresh)
    cv2.imshow("img_approx_points", img_approx_points)
    cv2.imshow("img_approx_line", img_approx_line)
    cv2.imshow("img_unified", img_unified)
    k = cv2.waitKey(25) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()
