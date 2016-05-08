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
        for row in range(0, self.height):
            for col in range(0, self.width):
                for i in range(0, 3):
                    self.image[row, col][i] = 255 - int(self.image[row, col][i])

    def toBlur(self):
        pass        
    
    def toTint(self, r, g, b):
        for row in range(0, self.height):
            for col in range(0, self.width):
                pixel = self.image[row, col]
                if pixel[0] <= 50:                
                    print '______________'
                    print pixel[0]
                    print pixel[0]+r
                self.image[row, col][0] = min(pixel[0]+r, 255)
                self.image[row, col][0] = max(pixel[0]+r, 0)
                self.image[row, col][1] = min(pixel[1]+g, 255)
                self.image[row, col][1] = max(pixel[1]+g, 0)
                self.image[row, col][2] = min(pixel[2]+b, 255)
                self.image[row, col][2] = max(pixel[2]+b, 0)
    
    def show(self):
        viewer = ImageViewer(self.image)
        viewer.show()
        
    
if __name__ == "__main__":
    filename = os.path.join('C:\Users\Dave Ho\ZetaPhase\ZetaPic\ZetaPic\www\samplePics\grapes.jpg')
    grape = io.imread(filename)
    grapes = Image(grape)
    
