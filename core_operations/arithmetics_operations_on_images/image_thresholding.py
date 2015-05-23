# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:28:29 2015

@author: Johnny

Illustrate image thresholding.

Inspired by:
http://opencvpython.blogspot.co.uk/2013/05/thresholding.html
"""
#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
#%%
# Read grayscale image. OK if not return None.
img = cv2.imread('messi_grayscale.jpg',0)
print img is not None
#%%
# refer to http://docs.opencv.org/doc/tutorials/imgproc/threshold/threshold.html
# ret,threshold_image = cv2.threshold(gray_scale_image,threshold,resolved_value,option)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)  # if greater than threshold, make it 255 (white). Otherwise, 0 (black)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) # inverse above.
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)  # If greater than threshold, make it threshold. Otherwise, leave as it is.
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)  # if greater than threshold, leave as it is. Otherwise, 0 (black)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)  #  # if greater than threshold, 0 (black). Otherwise, lave as it is.
#%%
thresh = ['img','thresh1','thresh2','thresh3','thresh4','thresh5']
thresh_dict = {
'img':'grayscale image',
'thresh1': 'THRESH_BINARY',
'thresh2': 'THRESH_BINARY_INV',
'thresh3': 'THRESH_TRUNC',
'thresh4': 'THRESH_TOZERO',
'thresh5': 'THRESH_TOZERO_INV'
}
#%%
for i in thresh:
    plt.imshow(eval(i),'gray')
    #plt.subplot(2,3,i+1),plt.imshow(eval(thresh[i]),'gray')
    plt.title(i + ": " + thresh_dict[i])
    plt.tight_layout() 
    plt.show()


