from app import PreprocessingAlgorithm
# Import necessary libraries
from skimage import io, filters,restoration
import matplotlib.pyplot as plt
import numpy as np
class MedianSmoothing(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,True)
        # Apply median filter to remove noise
        smoothed_image = filters.median(image)
        # smoothed_image = restoration.denoise_nl_means(image, h=0.1, fast_mode=True, patch_size=5, patch_distance=6)
        # smoothed_image = restoration.denoise_bilateral(image, sigma_color=0.05, sigma_spatial=15)
        # smoothed_image = filters.gaussian(image, sigma=1)
        # smoothed_image = restoration.denoise_wavelet(image, method='BayesShrink', mode='soft', rescale_sigma=True)


        
        self.show_images([image, smoothed_image ], titles=['Original', 'smoothed_image'])
        