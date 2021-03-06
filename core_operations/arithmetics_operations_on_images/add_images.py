# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:03:32 2015

@author: Johnny
"""

import cv2


# Image Blending (with weights in image 1 and image 2)
img1 = cv2.imread("iron_man_400px_by_500px.png")
print img1 is not None

img2 = cv2.imread("tony_stark_400px_by_500px.png")
print img2 is not None

dst = cv2.add(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("cv2.add img1 and img2", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
