# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:57:02 2015

@author: Johnny
"""

#%%
import cv2
import numpy as np

#%%
# mage Addition
# There is a difference between OpenCV addition and Numpy addition. 
# - OpenCV addition is a saturated operation  (clamped between min and max)
# - Numpy addition is a modulo operation.  (number gets recycle after hitting min / max)

# Note: uint8 type contains 2**8 = 256 integers. Ranging between 0 and 255.
#%%
x = np.uint8([250])
x
#%%
y = np.uint8([10])
y
#%%
#%%
# cv2 addition is clamped between min and max (think color scale)
print cv2.add(x,y) # 250+10 = 260 => 255  (max)
#%%
# NumPy addition is modulo - like a clock.
print x+y          # 250+10 = 260 % 256 = 4   (255 + 4 = 260)