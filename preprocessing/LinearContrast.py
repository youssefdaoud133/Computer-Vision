from app import PreprocessingAlgorithm
from skimage import io,exposure
import matplotlib.pyplot as plt
import numpy as np

class LinearContrast(PreprocessingAlgorithm):
    def ApplyAlgo(self, img):
        image = self.loadImage(img,False)
        # Calculate percentiles
        p2, p98 = np.percentile(image, (2, 98))
        print(p98)


        # Apply contrast stretching (linear transformation)
        stretched_image = exposure.rescale_intensity(image, in_range=(p2, p98))
        self.show_images([image, stretched_image ], titles=['Original', 'stretched_image'])
        