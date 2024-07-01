from skimage import io, img_as_ubyte
from matplotlib import pyplot as plt
import numpy as np

# Read the image
img = io.imread("./coffee.jpeg")

# Check if the image is read correctly
if img is None:
    print("Error: Image not found or could not be read.")
else:
    print(f"Original image dtype: {img.dtype}, shape: {img.shape}")

    # Convert image to 8-bit unsigned byte format
    img_as_8byte = img_as_ubyte(img)
    # print(f"Converted image dtype: {img_as_8byte.dtype}, shape: {img_as_8byte.shape}")

    # # Plot the histogram
    # plt.hist(img_as_8byte.flat, bins=100, range=(0, 255))
    # plt.title("Histogram of Image")
    # plt.xlabel("Pixel value")
    # plt.ylabel("Frequency")
    # plt.show()
        # Calculate the histogram
    hist, bin_edges = np.histogram(img_as_8byte, bins=256, range=(0, 255))

    # Plot the histogram
    plt.hist(img_as_8byte.flat, bins=256, range=(0, 255))
    plt.title("Histogram of Image")
    plt.xlabel("Pixel value")
    plt.ylabel("Frequency")
    plt.show()

    # Normalize the histogram
    hist_normalized = hist / np.sum(hist)

    # Define a threshold to split the histogram into dark and light pixels
    threshold = 127

    # Calculate the percentage of dark and light pixels
    dark_pixels_percentage = np.sum(hist_normalized[:threshold])
    light_pixels_percentage = np.sum(hist_normalized[threshold:])

    print(f"Dark pixels percentage: {dark_pixels_percentage * 100:.2f}%")
    print(f"Light pixels percentage: {light_pixels_percentage * 100:.2f}%")

    # Determine if the image is dark or light based on the percentages
    if dark_pixels_percentage > light_pixels_percentage:
        print("The image is dark.")
    else:
        print("The image is light.")
