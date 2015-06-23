# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:33:49 2015
Visualize convexity defect.
@author: Johnny
"""

import cv2
import numpy as np

def vis_convexity_defect(image_file):

    img = cv2.imread(image_file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 50, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt = contours[0]

    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(img, start, end, [0, 255, 0], 2)
        cv2.circle(img, far, 5, [0, 0, 255], -1)

    iname = 'Convexity Defect - ' + image_file
    cv2.imshow(iname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Build a list of image names to test - these files must exist in curret working directory.
image_files = []
for i in range(8):
    image_file = 'blue' + str(i) + '.png'
    image_files.append(image_file)

# Inline code to test run a series of images
for image_file in image_files:
    vis_convexity_defect(image_file)
