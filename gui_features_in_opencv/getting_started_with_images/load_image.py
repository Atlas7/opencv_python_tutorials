# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:04:13 2015

@author: Johnny

"""

#%%
import os
import numpy as np
import cv2

#%%
# Load an color image. 2nd arg: 1 = color, 0 = grayscale, -1 = unchanged)
img = cv2.imread("messi.jpg", 0)
#print img

#%% 
# Display an image
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite("messi_grayscale.jpg",img)

cv2.destroyAllWindows()
