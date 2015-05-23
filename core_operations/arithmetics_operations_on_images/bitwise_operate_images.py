# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:10:26 2015

@author: Johnny
Inspired by:
https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#image-arithmetics
"""

#%%
import numpy as np
import cv2
#%%
# Load image - messi
img1 = cv2.imread('messi_717px_by_483px.png')
print img1 is not None
cv2.imshow("img1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# load image - opencv logo
#img2 = cv2.imread('opencv_logo_white_background.png')
img2 = cv2.imread('opencv_logo_black_background.png')
print img2 is not None
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
print (rows,cols,channels)
#%%
roi = img1[0:rows, 0:cols ]
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2gray", img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# If white (255), leave it as it is. Else, make it black (0).
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# Invert: white become black, and black become white
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv", mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow("img1_bg", img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow("img2_fg", img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
img1[0:rows, 0:cols] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
