# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:33:15 2015
Illustrate converting from GBR to HSV color space.
@author: Johnny
"""

import cv2
import numpy as np

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
# [[[ 60 255 255]]]