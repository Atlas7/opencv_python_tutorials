# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:12:08 2015
Illustrate rotation of an image.
@author: Johnny
"""

import cv2

#%%
img = cv2.imread('messi.jpg',0)
print img is not None
#%%
cv2.imshow("img",img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
rows,cols = img.shape
print (cols, rows)
#%%
# cv2.getRotationMatrix2D((x_center, y_center),degree_rotation_anticlockwise,scale)
# Default center location is top-left of image.
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
M
#%%
dst = cv2.warpAffine(img,M,(cols,rows))
dst
#%%
cv2.imshow("dst",dst)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()