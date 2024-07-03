from app import PreprocessingAlgorithm
# Import necessary libraries
from skimage import io,restoration , color, filters, morphology, feature
import matplotlib.pyplot as plt
from skimage.filters import sobel,threshold_otsu
from scipy.signal import convolve2d
from skimage.feature import canny
from scipy import ndimage as ndi

import numpy as np
class BackGroundSeperation(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,True)
        # Compute the Otsu threshold
        thresh_value = threshold_otsu(image)
        
        mask = image < thresh_value

        seperatedImage = np.ones_like(image)
        seperatedImage[mask] = image[mask]

        
        self.show_images([image, seperatedImage ], titles=['Original', 'SeperateBackground'])
        