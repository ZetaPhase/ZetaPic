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
    
    def show(self):
        viewer = ImageViewer(self.image)
        viewer.show()

def toGrayscale(image):
    for row in range(0, int(grapes.shape[0])):
        for col in range(0, int(grapes.shape[1])):
            average = image[row, col][0] + image[row, col][1] + image[row, col][2]
            image[row, col] = (average, average, average)
    
            
def toInverted(image):
    for row in range(0, int(grapes.shape[0])):
        for col in range(0, int(grapes.shape[1])):
            for i in range(0, 3):
                image[row, col][i] = 255 - int(image[row, col][i])

def show(image):
    viewer = ImageViewer(image)
    viewer.show()
    
if __name__ == "__main__":
    filename = os.path.join(skimage.data_dir, 'grapes.jpg')
    grape = io.imread(filename)
    grapes = Image(grape)
    
