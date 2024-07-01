from app import PreprocessingAlgorithm
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

class GammaCorrection(PreprocessingAlgorithm):
    def ApplyAlgo(self, img , Gamma):
        image = self.loadImage(img,True)
        

        # Apply the Gamma correction transformation
        gamma_image = np.power(image,Gamma)
        self.show_images([image, gamma_image ], titles=['Original', 'gamma_image'])
        