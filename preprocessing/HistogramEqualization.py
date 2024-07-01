from app import PreprocessingAlgorithm
from skimage import io,exposure,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

class HistogramEqualization(PreprocessingAlgorithm):
    def ApplyAlgo(self, img ):
        
        image = self.loadImage(img,True)
        # Apply histogram equalization
        equalized_image = exposure.equalize_hist(image)
        img_as_8byte = img_as_ubyte(equalized_image)
        hist, bin_edges = np.histogram(img_as_8byte, bins=256, range=(0, 255))
 
        # plt.hist(img_as_8byte.flat, bins=256, range=(0, 255))
        # plt.title("Histogram of Image")
        # plt.xlabel("Pixel value")
        # plt.ylabel("Frequency")
        # plt.show()
        self.show_images([image, equalized_image ], titles=['Original', 'equalized_image'])
        