from abc import ABC, abstractmethod
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import median, sobel
from skimage.feature import canny
from scipy.signal import convolve2d
from scipy import fftpack

class PreprocessingAlgorithm(ABC):
    @abstractmethod
    def ApplyAlgo(self, img):
        pass
    def loadImage(self,img,isGray):
        # Load the image
        image = io.imread(img, as_gray=isGray)
        return image
    # Show the figures / plots inside the notebook
    def show_images(self,images,titles=None):
        #This function is used to show image(s) with titles by sending an array of images and an array of associated titles.
        n_ims = len(images)
        if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
        fig = plt.figure()
        n = 1
        for image,title in zip(images,titles):
            a = fig.add_subplot(1,n_ims,n)
            if image.ndim == 2: 
                plt.gray()
            plt.imshow(image)
            a.set_title(title)
            plt.axis('off')
            n += 1
        fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
        plt.show() 