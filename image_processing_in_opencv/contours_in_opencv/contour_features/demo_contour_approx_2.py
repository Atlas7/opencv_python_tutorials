# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015

@author: Johnny
"""

#%%
import cv2
import numpy as np

#%%
img = cv2.imread('plate.jpg')
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
#%%
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray", img_gray)
cv2.waitKey()
cv2.imwrite("img_gray.jpg", img_gray)
cv2.destroyAllWindows()
#%%
ret, img_thresh = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow("img_thresh", img_thresh)
cv2.waitKey()
cv2.imwrite("img_thresh.jpg", img_thresh)
cv2.destroyAllWindows()
#%%
img_contours, contours, hierarchy = cv2.findContours(img_thresh, 1, 2)
#img_contours, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("img_contours", img_contours)
cv2.waitKey()
cv2.imwrite("img_contours.jpg", img_contours)
cv2.destroyAllWindows()
#%%
# create a new blank window for drawing onto
img_blank = np.zeros(img.shape, np.uint8)
img_blank.shape
cv2.imshow("img_blank", img_blank)
cv2.waitKey()
cv2.imwrite("img_blank.jpg", img_blank)
cv2.destroyAllWindows()
#%%
img_contours2 = img_blank.copy()
cv2.drawContours(img_contours2, contours, -1, (0, 255, 0), 1)
cv2.imshow("img_contours2", img_contours2)
cv2.waitKey()
cv2.imwrite("img_contours2.jpg", img_contours2)
cv2.destroyAllWindows()
#%%
for h, cnt in enumerate(contours):
    # Pick a contour segment in the definition of arch length
    perimeter = cv2.arcLength(cnt, True)
    print perimeter
    
    #epsilon = 0.1*perimeter
    epsilon = 0.1*perimeter
    print epsilon
    
    # Generate the approximated curve by removing the "cracks" (or deviations)
    contour_approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    img_contours_approx = img_blank.copy()
    cv2.drawContours(img_contours_approx, contour_approx, -1, (0, 255, 0), 1)
    cv2.imshow("img_contours_approx", img_contours_approx)
    cv2.waitKey()
    cv2.imwrite("img_contours_approx.jpg", img_contours_approx)
cv2.destroyAllWindows()
#%%
# create a new image to draw the approx curve on
img_approx = np.zeros(img.shape, np.uint8)
img_approx.shape
#%%
# Plot the approx curve to see what it looks like
n = len(contour_approx)
for i in range(n):
    i0 = i
    i1 = i0 + 1
    if i1 == n:
        i1 = 0
    p0 = tuple(contour_approx[i0][0])
    p1 = tuple(contour_approx[i1][0])
    print "start: " + str(p0) + " ; end: " + str(p1)
    img_approx = cv2.line(img_approx, p0, p1,(255,0,0), 1)
    
cv2.imshow("img_approx", img_approx)
cv2.waitKey()
cv2.imwrite("img_approx.jpg", img_approx)
cv2.destroyAllWindows()

