# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:37:07 2016

@author: daveho8888
"""

import numpy as np
import os
import skimage
from skimage import data
from skimage import novice
from skimage import io
from skimage.viewer import ImageViewer

class Image:
    def __init__(self, image):
        self.image = np.copy(image)
        self.original = np.copy(image)
        self.width = int(image.shape[1])
        self.height = int(image.shape[0])
    
    def reset(self):
        self.image = np.copy(self.original)
        
    def toGrayScale(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                average = (self.image[row, col][0] + self.image[row, col][1] + self.image[row, col][2])/3.0
                self.image[row, col] = (average, average, average)
    
    def toInverted(self):
        tmp = np.array([255, 255, 255])
        tmp = tmp.astype('uint8')
        self.image = tmp - self.image

    def toBlur(self):
        pass        
    
    def toTint(self, r, g, b):
        self.image = self.image.astype('int32') + np.array([r, g, b]).astype('int32')
        self.image = np.clip(self.image, 0, 255)
        self.image = self.image.astype('uint8')

    def show(self):
        viewer = ImageViewer(self.image)
        viewer.show()
        
    
if __name__ == "__main__":
    filename = os.path.join('C:\Users\Dave Ho\ZetaPhase\ZetaPic\ZetaPic\www\samplePics\grapes.jpg')
    grape = io.imread(filename)
    grapes = Image(grape)
    
