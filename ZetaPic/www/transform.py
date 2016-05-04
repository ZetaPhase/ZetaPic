# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:37:07 2016

@author: daveho8888
"""

import os
import skimage
from skimage import data
from skimage import novice
from skimage import io
from skimage.viewer import ImageViewer

def toGrayscale(image):
    for row in range(0, len(int(grapes.shape[0]))):
        for col in range(0, len(int(grapes.shape[1]))):
            average = image[row, col][0] + image[row, col][1] + image[row, col][2]
            image[row, col] = (average, average, average)
            
def show(image):
    viewer = ImageViewer(image)
    viewer.show()
