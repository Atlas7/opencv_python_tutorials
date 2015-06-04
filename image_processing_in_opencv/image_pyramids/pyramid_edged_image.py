# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 14:12:15 2015
Illusrate the use of cv2.pyrDown to lower resolution and 
cv2.pyrUp to increase resolution - against edged images.
@author: Johnny
"""

import cv2


img = cv2.imread('messi.jpg', 0)
edges = cv2.Canny(img, 100, 200)
d1u0 = cv2.pyrDown(edges)
d2u0 = cv2.pyrDown(d1u0)
d3u0 = cv2.pyrDown(d2u0)
d3u1 = cv2.pyrUp(d3u0)
d3u2 = cv2.pyrUp(d3u1)
d3u3 = cv2.pyrUp(d3u2)

# display images
cv2.imshow('edges', edges)
cv2.imshow('d1u0', d1u0)
cv2.imshow('d2u0', d2u0)
cv2.imshow('d3u0', d3u0)
cv2.imshow('d3u1', d3u1)
cv2.imshow('d3p2', d3u2)
cv2.imshow('d3u3', d3u3)

# hit any keys to close the displayed images
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
