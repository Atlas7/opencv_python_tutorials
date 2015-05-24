# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:01:10 2015

@author: Johnny
"""

import cv2
import numpy as np

#%%
img = cv2.imread('messi.jpg')
print img is not None
cv2.imshow("img",img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("res",res)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow("res",res)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()