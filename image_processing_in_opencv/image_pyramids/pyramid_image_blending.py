# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 19:32:01 2015

@author: Johnny

This is taken from the OpenCV-Python Tutorials.
Illustrate Image blend with Laplacian Pyrimaid Image Blending.

References:

    https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_pyramids/py_pyramids.html#pyramids
    http://pages.cs.wisc.edu/~csverma/CS766_09/ImageMosaic/imagemosaic.html

"""
#%%
import cv2
import numpy as np

#%% set pyramid level
n = 3

#%%
A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')

#%%
# generate Gaussian pyramid for A - from base to tip.
G = A.copy()
gpA = [G]
for i in xrange(n):
    G = cv2.pyrDown(G)
    gpA.append(G)


#%%

# generate Gaussian pyramid for B - from base to tip.
G = B.copy()
gpB = [G]
for i in xrange(n):
    G = cv2.pyrDown(G)
    gpB.append(G)

#%%
# generate Laplacian Pyramid for A - from tip to base
lpA = [gpA[n]]
for i in xrange(n, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)
#%%
# generate Laplacian Pyramid for B - from tip to base
lpB = [gpB[n]]
for i in xrange(n, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

#%%
# Now add left and right halves of images in each level - from tip to base.
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols/2], lb[:, cols/2:]))
    LS.append(ls)

#%%
# now reconstruct (Laplacian Pyramid Blending) - tip to base.
ls_ = LS[0]
for i in xrange(1, n+1):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

#%%
# image with direct connecting each half
real = np.hstack((A[:, :cols/2], B[:, cols/2:]))

#%%
# Display images. Hit any keys to close the displayed images
cv2.imshow('Left Image', A)
cv2.imshow('Right Image', B)
cv2.imshow('Pyramid Blending', ls_)
cv2.imshow('Direct Connection', real)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
