# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:34:32 2015
A Contour Class that describe contour properties and methods.
Limitations:
- can only take on an image that contains 1 contour line.
@author: Johnny
"""
#%%
import cv2
import numpy as np


class Contour(object):

    def __init__(self, an_image_file):

        self.file_name = an_image_file
        self.img = self.get_img(self.file_name)
        self.img_gray = self.get_img_gray(self.img)
        self.img_thresh = self.get_img_thresh(self.img_gray)
        self.coordinates = self.get_coordinates(self.img_thresh)
        self.aspect_ratio = self.get_aspect_ratio(self.coordinates)
        self.extent = self.get_extent(self.coordinates)
        self.solidity = self.get_solidity(self.coordinates)
        self.equivalent_diameter = self.get_equivalent_diameter(self.coordinates)
        self.area = self.get_area(self.coordinates)
        self.orientation = self.get_orientation(self.coordinates)
        self.mask = self.get_mask(self.img_gray, self.coordinates)
        self.pixel_points = self.get_pixel_points(self.img_gray, self.mask)
        self.min_max_loc = self.get_min_max_loc(self.img_gray, self.mask)
        self.mean_val = self.get_mean_val(self.img, self.mask)
        self.extreme_points = self.get_extream_points(self.coordinates)

    def get_img(self, an_image_file):
        img = cv2.imread(an_image_file)
        return img

    def get_img_gray(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray

    def get_img_thresh(self, img_gray):
        ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
        return img_thresh

    def get_coordinates(self, img_thresh):
        image, contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours[0]

    def get_aspect_ratio(self, cnt):
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        return aspect_ratio

    def get_extent(self, cnt):
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w*h
        extent = float(area) / rect_area
        return extent

    def get_solidity(self, cnt):
        area = cv2.contourArea(cnt)
        hull = cv2.convexHull(cnt)
        hull_area = cv2.contourArea(hull)
        solidity = float(area)/hull_area
        return solidity

    def get_equivalent_diameter(self, cnt):
        area = cv2.contourArea(cnt)
        equivalent_diameter = np.sqrt(4*area/np.pi)
        return equivalent_diameter

    def get_area(self, cnt):
        area = cv2.contourArea(cnt)
        return area

    def get_orientation(self, cnt):
        (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
        orientation = ((x, y), (MA, ma), angle)
        return orientation

    def get_mask(self, img_gray, cnt):
        mask = np.zeros(img_gray.shape, np.uint8)
        cv2.drawContours(mask, [cnt], 0, 255, -1)
        return mask

    def get_pixel_points(self, img_gray, mask):
        pixel_points = np.transpose(np.nonzero(mask))
        # pixel_points = cv2.findNonZero(mask)
        return pixel_points

    def get_min_max_loc(self, img_gray, mask):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_gray, mask=mask)
        min_max_loc = (min_val, max_val, min_loc, max_loc)
        return min_max_loc

    def get_mean_val(self, img, mask):
        mean_val = cv2.mean(img, mask=mask)
        return mean_val

    def get_extream_points(self, cnt):
        leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
        rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
        topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
        bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
        return (leftmost, rightmost, topmost, bottommost)

    def show_image(self, img):
        cv2.imshow("img", img)
        cv2.waitKey()
        cv2.destroyAllWindows()

#%%
# Inline code
if __name__ == '__main__':
    a = Contour("blue_thunder.png")
    print(a.file_name)
    print(len(a.coordinates))
    print(a.aspect_ratio)
    print(a.extent)
    print(a.solidity)
    print(a.equivalent_diameter)
    print(a.area)
    print(a.orientation)
    print(len(a.pixel_points), " ", a.pixel_points[0])
    print(a.min_max_loc)
    print(a.mean_val)
    print(a.extreme_points)
