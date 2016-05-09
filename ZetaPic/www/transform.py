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
from PIL import Image

class Picture:
    def __init__(self, image):
        self.image = np.copy(image)
        self.original = np.copy(image)
        self.width = int(image.shape[1])
        self.height = int(image.shape[0])
    
    def reset(self):
        self.image = np.copy(self.original)
        
    def toGrayScale(self):
        layer = np.mean(self.image.astype('int32'), axis=2)
        self.image = np.repeat(layer, 3, axis=1)
        self.image.shape = (1067L, 1600L, 3L)
        self.image = self.image.astype('uint8')
    
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
    grapes = Picture(grape)
    
