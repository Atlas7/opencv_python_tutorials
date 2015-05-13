# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:04:13 2015

@author: Johnny

The program:

- is designed to be run via an IDE (e.g. Spyder).
- loads and display an image.
"""

#%%
import os
import numpy as np
import cv2

#%% 
# If run in IDE, we need to set work directory
os.getcwd()
os.chdir(r"C:\Users\Johnny\version-control\opencv_python_tutorials\gui_features_in_opencv\getting_started_with_images")
os.getcwd()

#%%
# Load an color image in grayscale
img = cv2.imread(r"messi_hd.jpg", 0)
print img

#%%
# required if run in IDE. e.g. Spyder.
cv2.startWindowThread() 

# enable resizing. Handy for very large image.
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 

# Display an image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
