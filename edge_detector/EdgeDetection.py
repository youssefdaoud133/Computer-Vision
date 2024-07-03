from app import PreprocessingAlgorithm
# Import necessary libraries
from skimage import io, filters,restoration
import matplotlib.pyplot as plt
from skimage.filters import sobel
from scipy.signal import convolve2d
from skimage.feature import canny

import numpy as np
class EdgeDetection(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,True)
        # Apply median filter to remove noise
        # smoothed_image = filters.median(image)
        # # Apply Sobel operator for edge detection
        # edges = filters.sobel(smoothed_image)
        # Define Roberts operator kernels
        # roberts_cross_v = np.array([[1, 0], [0, -1]])
        # roberts_cross_h = np.array([[0, 1], [-1, 0]])

        # # Apply the Roberts operator using convolution
        # vertical_edges = convolve2d(image, roberts_cross_v, mode='same', boundary='fill', fillvalue=0)
        # horizontal_edges = convolve2d(image, roberts_cross_h, mode='same', boundary='fill', fillvalue=0)

        # # Combine the results to get the final edge-detected image
        # edge_roberts = np.sqrt(vertical_edges**2 + horizontal_edges**2)
        # Define Prewitt operator kernels
        # prewitt_kernel_v = np.array([[1, 0, -1],
        #                             [1, 0, -1],
        #                             [1, 0, -1]])

        # prewitt_kernel_h = np.array([[1, 1, 1],
        #                             [0, 0, 0],
        #                             [-1, -1, -1]])

        # # Apply the Prewitt operator using convolution
        # vertical_edges = convolve2d(image, prewitt_kernel_v, mode='same', boundary='fill', fillvalue=0)
        # horizontal_edges = convolve2d(image, prewitt_kernel_h, mode='same', boundary='fill', fillvalue=0)

        # # Combine the results to get the final edge-detected image
        # edge_prewitt = np.sqrt(vertical_edges**2 + horizontal_edges**2)
        # Apply the Canny edge detector
        edges = canny(image, sigma=1)
    

        
        self.show_images([image, 255-edges ], titles=['Original', 'edges'])
        