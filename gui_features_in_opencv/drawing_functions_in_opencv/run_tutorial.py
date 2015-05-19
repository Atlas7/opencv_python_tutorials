# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:06:43 2015

@author: Johnny
"""

#%%
import numpy as np
import cv2
#%%
# Create a black image
# initialize the image as a box of 512 units (height) by 512 units (width) by 3 units (BGR tuple). 
# Each value is of type numpy.unit8 (unsigned integer ranging between 0 to 255)
img = np.zeros((512,512,3), np.uint8)
#%%
print img.shape
#>>> (512L, 512L, 3L)
#%%
# Draw shapes.
# Notes: a 2-D coordinate tuple is in (x, y)
#%%
# Draw a diagonal blue line with thickness of 5 px
# Essentially update img like this:
# img = cv2.line(image_to_draw_on, start_coordinate, end_coordinate, BGR_tuple, thickness_in_pixels)
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#%%
# Draw a rectangle with thickness of 3 px
# Essentially update img like this:
# img = cv2.rectangle(image_to_draw_on, top_left_coordinate, bottom_right_coordinate, BGR_tuple, thickness_in_pixels)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#%%
# Draw a circle with thickness of 1 px (inwards - indicated by the negative sign thickness)
# Essentially update img like this:
# img = cv2.circle(image_to_draw_on, center_coordinate, radius, BGR_tuple, thickness_in_pixels)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#%%
# Draw an ellipse with thickness of 1 px (inwards - indicated by the negative sign thickness)
# Essentially update img like this:
# cv2.ellipse(image_to_draw_on, center_coordinate, (axis_a_length, axis_b_length), angle, startAngle, endAngle, color, thickness)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#%%
# Draw a polyline
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print pts
pts = pts.reshape((-1,1,2))
print "---"
print pts
cv2.polylines(img,[pts],True,(0,255,255))
#%%
# Draw text
font = cv2.FONT_HERSHEY_SIMPLEX
# Python 3.x version uses cv2.LINE_AA 
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
# Python 2.x version uses cv2.CV_AA
#cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.CV_AA)
#%%
# Display image in a window.

# Optional:
#cv2.startWindowThread() 
# Optional: enable resizing. Handy for very large image.
#cv2.namedWindow('img', cv2.WINDOW_NORMAL) 
# Display an image
cv2.imshow('img',img)

#  's' to save.
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite("output.jpg",img)

cv2.destroyAllWindows()    
    
