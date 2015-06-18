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
for pt in pts:
    cv2.circle(img, pts[pt], 3, (0, 0, 255), -1)
    cv2.putText(img, pt, pts[pt], cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
