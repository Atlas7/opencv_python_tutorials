# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:34:32 2015
A Contour Class that describe contour properties and methods.
Limitations:
- can only take on an image that contains 1 contour line.
@author: Johnny
"""
#%%
import cv2
import numpy as np


class Contour(object):
    
    def __init__(self, an_image_file):
        
        self.file_name = an_image_file       
        self.set_coordinates(self.file_name)
        self.set_aspect_ratio(self.coordinates)
        self.set_extent(self.coordinates)
        
    def set_coordinates(self, an_image_file):
        # Define the first contour line
        img = cv2.imread(an_image_file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
        image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.coordinates = contours[0]

    def set_aspect_ratio(self, cnt):
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        self.aspect_ratio = aspect_ratio

    def set_extent(self, cnt):
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w*h
        extent = float(area) / rect_area
        self.extent = extent

#%%
# Inline code
if __name__ == '__main__':
    a = Contour("blue_thunder.png")
    print(a.file_name)
    print(len(a.coordinates))
    print(a.aspect_ratio)
    print(a.extent)