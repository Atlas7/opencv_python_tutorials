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
# If run in IDE, we need to set work directory. Uncomment and update below.
os.getcwd()
os.chdir(r"C:\Users\Johnny\version-control\opencv_python_tutorials\gui_features_in_opencv\getting_started_with_images")
os.getcwd()

#%%
# Load an color image. 2nd arg: 1 = color, 0 = grayscale, -1 = unchanged)
img = cv2.imread(r"messi_hd.jpg", 0)
print img

#%% 
""" 
Run this cell in interactive mode to see the loaded image.
Not required in batch mode.
"""
# Required if run in IDE. e.g. Spyder.
cv2.startWindowThread() 
# Enable resizing. Handy for very large image.
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
# Display an image
cv2.imshow('image',img)

#%%
#  ESC key to exit, or 's' to save.
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(r"messi_hd_grayscale.jpg",img)
    cv2.destroyAllWindows()
