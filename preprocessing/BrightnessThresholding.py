from app import PreprocessingAlgorithm
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

class BrightnessThresholding(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,False)


        # Define the brightness threshold
        threshold = 50  # Adjust this value as needed

        # Apply the brightness thresholding transformation
        thresholded_image = np.where(image> threshold , 255 , 0)
        self.show_images([image, thresholded_image ], titles=['Original', 'thresholded_image'])
        