# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:08:40 2015

@author: Johnny
"""
#%%
#Accessing and Modifying pixel values
#%%
import cv2
import numpy as np

#%%
img = cv2.imread('messi.jpg')

#%%
print img
#%%
cv2.imshow('original image',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
# Access pixe lBGR values at row 100 (y), column 150 (x) 
px = img[100,150]
print px
#%%
# accessing only blue pixel at row 100 (y), column 150 (x) 
blue = img[100,150,0]
print blue
#%%
# Modify pixel BGR value at row 100 (y), column 150 (x) - to white.
img[100,150] = [255,255,255]
print img[100,150]
# show modified image
cv2.imshow('add a white pixel at row 100, column 150',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
#Better pixel accessing and editing method
print img.item(10,20,2)
# modifying BGR red value using the better accessin method
img.itemset((10,20,2),255)
print img.item(10,10,2)
#%%
# show modified image
cv2.imshow('add a red pixel at row 100, column 150',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
#Accessing Image Properties
#%%
# Access image property - shape
print img.shape
#%%
# Total number of pixels
print img.size
#%%
# Image datatype
print img.dtype
#%%
# Image ROI (region of interest)
#%%
# Select the ball from the image (use the Windows Paint App to find ball location)
ball = img[398:468,438:521]
# Show the ball
cv2.imshow('show the ball only',ball)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
#Copy the ball to a different region of the picture
img[198:268,238:321] = ball
cv2.imshow('copy and paste the ball to somewhere else',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
# Splitting and Merging Image Channels
b,g,r = cv2.split(img)
img_split_merge = cv2.merge((b,g,r))
print img_split_merge
cv2.imshow('image after split and merge',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%
# Access all the blue pixels
b = img[:,:,0]
print b
#%%
# Change all the red pixel to white
img[:,:,2] = 0
cv2.imshow('reduce the BGR red scale to 0',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
#%%