# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:12:03 2015
Illustrate smoothing of an image with 2D Convolution.
@author: Johnny
"""
#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
#%%
img_bgr = cv2.imread('opencv_logo_black_background.png')
print img_bgr is not None
#%%
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
#%%
blur_rgb = cv2.blur(img_rgb,(5,5))
#%%
plt.subplot(121),plt.imshow(img_rgb),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur_rgb),plt.title('cv2.blur')
plt.xticks([]), plt.yticks([])
plt.show()
