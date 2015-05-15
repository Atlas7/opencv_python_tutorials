# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:10:14 2015

@author: Johnny
"""

#%%
import numpy as np
import cv2

#%%
#cap = cv2.VideoCapture("all_blacks_skills_part_2.mp4")
cap = cv2.VideoCapture(r"C:\Users\Johnny\version-control\sources\opencv_python_tutorials\gui_features_in_opencv\getting_started_with_videos\all_blacks_skills_part_2.mp4")
#%%
cap
#%%
print cap.isOpened()
#%%
# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
#%%
#out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,360))
out = cv2.VideoWriter(r"C:\Users\Johnny\version-control\sources\opencv_python_tutorials\gui_features_in_opencv\getting_started_with_videos\output.avi",fourcc, 20.0, (640,360))
#%%
print out.isOpened()
#%%
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#%%
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
