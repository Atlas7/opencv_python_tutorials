# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:56:33 2015
My attempt to create a sample grayscale sample image for the image 
thresholding exercises.
@author: Johnny
"""

#%%
import numpy as np
import cv2
#%%
# Create a list containing the 256 (grascale) scalar
line = []
for i in xrange(256):
    line.append(i)
#%%
# Repeat this line for many rows. So we have a n-by-n list
line_page = []
for i in xrange(len(line)):
    line_page.append(line)
#%%
# Convert the n-by-n list to a NumMpy array
img = np.asarray(line_page, dtype=np.uint8)
print img
print img.shape
print img.dtype
#%%
# Show image. type "s" to save image.
cv2.imshow("img_grayscale", img)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite("gradient.png",img)    
cv2.destroyAllWindows()