# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:38:04 2015

@author: Johnny

Print all available events to choose from.
"""

import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print events