# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:27:39 2015

@author: Johnny
"""
#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('messi.jpg')
if img is None:
    print "imread Failure"
else:    
    print "imread OK"

#%%
# cv2.copyMakeBorder(image,top,bottom,left,right,border_type)
replicate = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_CONSTANT,value=BLUE)

#%%
# show modified image
cv2.imshow('ORIGINAL',img1)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
cv2.imshow('cv2.BORDER_REPLICATE',replicate)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
cv2.imshow('cv2.BORDER_REFLECT',reflect)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
cv2.imshow('BORDER_REFLECT_101',reflect101)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
cv2.imshow('cv2.BORDER_WRAP',wrap)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
cv2.imshow('cv2.BORDER_CONSTANT (Blue)',constant)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#%%
#plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
#plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
#plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
#plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
#plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

#plt.show()