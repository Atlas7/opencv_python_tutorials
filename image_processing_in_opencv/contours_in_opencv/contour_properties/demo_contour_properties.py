# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:34:32 2015
Illustrate computation of various contour properties.
@author: Johnny
"""
#%%
import cv2
import numpy as np

#%%
def get_a_contour(an_image_file):
    img = cv2.imread(an_image_file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    return cnt

#%%
# Aspect Ratio
def get_aspect_ratio(a_contour):
    x,y,w,h = cv2.boundingRect(a_contour)
    aspect_ratio = float(w)/h
    return aspect_ratio

#%%
# Area
def get_area(a_contour):    
    area = cv2.contourArea(a_contour)
    x, y, w, h = cv2.boundingRect(a_contour)
    rect_area = w*h
    extent = float(area) / rect_area
    return extent

# Solidity
def get_solidity(a_contour):
    area = cv2.contourArea(a_contour)
    hull = cv2.convexHull(a_contour)
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area
    return solidity

#%%
# Inline code
cnt = get_a_contour("blue_thunder.png")
print("Aspect Ratio: ", get_aspect_ratio(cnt))
print("Extent: ", get_area(cnt))
