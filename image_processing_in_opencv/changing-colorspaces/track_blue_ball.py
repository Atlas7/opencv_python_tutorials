# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:39:27 2015

@author: Johnny
"""

import cv2
import numpy as np

#%%
cap = cv2.VideoCapture("big_blue_ball_machine_8HZPb7ulu08.mp4")
cap.isOpened()
#%%
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([96,41,44])
    upper_blue = np.array([160,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(25) & 0xFF == ord('q'):  # hit "q to exit.
        break

cv2.destroyAllWindows()