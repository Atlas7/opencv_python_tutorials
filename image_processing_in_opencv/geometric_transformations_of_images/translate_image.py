# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:02:49 2015
Illustrate translation of an image, using cv2.warpAffine.
@author: Johnny
"""

import cv2
import numpy as np

#%%
img = cv2.imread('messi.jpg',0)
print img is not None
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
rows,cols = img.shape
#%%
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

#%%
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()