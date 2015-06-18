# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:41:01 2015
Test playing with the Contour class (inspired by OpenCV-Python - Contour Properties lesson)
@author: Johnny
"""
#%%
from Contour import Contour
#%%
import cv2
import numpy as np
#%%
a = Contour("blue1.png")
#%%
pts = a.extreme_points
#%%
cnt = a.coordinates
#%%
img = a.img
#%%
pts_dict = {
    "left": pts[0], 
    "right": pts[1],
    "top": pts[2],
    "bottom": pts[3]
}
#%%
for pt in pts_dict:
    cv2.circle(img, pts_dict[pt], 3, (0, 0, 255), -1)
    cv2.putText(img, pt, pts_dict[pt], cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
