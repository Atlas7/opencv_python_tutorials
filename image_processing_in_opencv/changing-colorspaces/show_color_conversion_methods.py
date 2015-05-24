# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print flags
for i in flags:
    print i