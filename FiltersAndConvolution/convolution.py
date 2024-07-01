from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import median, sobel
from skimage.feature import canny
from scipy.signal import convolve2d
from scipy import fftpack


# Show the figures / plots inside the notebook
def show_images(images,titles=None):
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


# Function to apply filters and show images
def apply_filters(image_path):
    # Read the image
    img = io.imread(image_path, as_gray=True)
    
    # Apply median filter
    img_median = median(img)
    
    # Apply Canny edge detection
    edges = canny(img)
    
    # Show images using your show_images function
    show_images([img, img_median, edges], titles=['Original', 'Median Filtered', 'Canny Edges'])

# Example usage
image_path = './test1.jpg'
# apply_filters(image_path)


# Function to apply filters and show images
def apply_blur_filters(image_path):
    # Read the image
    img = io.imread(image_path, as_gray=True)
    
   # Define the blur kernel (1D)
    blur_kernel = np.ones((1, 8), dtype=np.float32) / 8.0

    # Apply horizontal blur
    img_blur_h = convolve2d(img, blur_kernel, mode='same', boundary='wrap')

    # Apply vertical blur
    img_blur_v = convolve2d(img, blur_kernel.T, mode='same', boundary='wrap')

    # Combine horizontal and vertical blur (optional for better effect)
    img_blur = (img_blur_h + img_blur_v) / 2.0
    show_images([img, img_blur ], titles=['Original', 'Blur Filtered'])


# Example usage
image_path = './test1.jpg'
# apply_blur_filters(image_path)

# Function to apply filters and show images
def detect_edges(image_path):
    # Read the image
    img = io.imread(image_path, as_gray=True)
    imgOriginal = io.imread(image_path, as_gray=False)

    
   # Define the blur kernel (1D)
    detect_kernel = np.array([[1, 1, 1],
                              [1, -8, 1],
                              [1, 1, 1]], dtype=np.float32) 

    # Apply horizontal blur
    img_detect_h = convolve2d(img, detect_kernel, mode='same', boundary='wrap')

    # Apply vertical blur
    img_detect_v = convolve2d(img, detect_kernel.T, mode='same', boundary='wrap')

      # Combine horizontal and vertical edge detection (optional for better effect)
    # img_detect = np.sqrt(img_detect_h**2 + img_detect_v**2)
    img_detect = np.sqrt(img_detect_h**2 + img_detect_v**2)


     # Create a copy of the original image to overlay edges
    img_edges = np.copy(imgOriginal)
    
    # Threshold for edge detection (optional)
    threshold = .8
    img_edges[img_detect > threshold] = [0, 255, 0]  # Overlay red color on edges


    show_images([imgOriginal, img_edges ], titles=['Original', 'img_detect Filtered'])


# Example usage
image_path = './test1.jpg'
# detect_edges(image_path)


# Function to apply Fourier transform and high-pass filter
def apply_high_pass_filter(image_path, cutoff_freq=0.1):
    # Read the image
    img_gray = io.imread(image_path, as_gray=True)

    
    # Compute 2D Fourier transform
    img_fft = fftpack.fft2(img_gray)
    
    # Shift zero frequency component to the center
    img_fft_shifted = fftpack.fftshift(img_fft)
    
    # Create high-pass filter (example: ideal high-pass filter)
    rows, cols = img_fft_shifted.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.ones_like(img_fft_shifted)
    radius = int(cutoff_freq * min(center_row, center_col))
    mask[center_row - radius:center_row + radius, center_col - radius:center_col + radius] = 0
    
    # Apply high-pass filter
    img_fft_shifted_filtered = img_fft_shifted * mask
    
    # Shift frequency components back
    img_fft_filtered = fftpack.ifftshift(img_fft_shifted_filtered)
    
    # Inverse Fourier transform
    img_filtered = np.abs(fftpack.ifft2(img_fft_filtered))
    
    # Normalize to range [0, 255] for display
    img_filtered = (img_filtered - np.min(img_filtered)) / (np.max(img_filtered) - np.min(img_filtered))
    img_filtered = (img_filtered * 255).astype(np.uint8)
    
    # Display original and filtered images
    show_images([img_gray, img_filtered], titles=['Original', 'High-Pass Filtered'])

# Example usage
image_path = './test1.jpg'
apply_high_pass_filter(image_path, cutoff_freq=0.1)