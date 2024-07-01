from app import PreprocessingAlgorithm
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

class NegativeTransformation(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,False)


        # Apply the negative transformation
        negative_image = 255 - image
        self.show_images([image, negative_image ], titles=['Original', 'negative_image'])
        