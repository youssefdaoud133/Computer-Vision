# Lecture 01: Introduction to Computer Vision

**Instructor:** Mayada Hadhoud  
**Department:** Computer Engineering, Cairo University

## Agenda
- What is Computer Vision?
- Difference between Computer Vision and Image Processing
- What is a Computer Vision System?
- Computer Vision Applications
- Image Formation
- Cameras
- Data Structures for Image Analysis
- Digital Image Properties

## Acknowledgement
Some slides are taken from the Computer Vision: Foundations and Applications Course by Stanford Vision and Learning Lab.

## What is Computer Vision?
- Automates tasks that the human visual system can do.
- Goal: Bridge the gap between pixels and meaning.

## Difference between Image Processing and Computer Vision
- **Image Processing:**
  - Input: Image
  - Output: Image
- **Computer Vision:**
  - Input: Image, image sequence, video
  - Output: Decision, classification, etc.
- Image processing is a part of computer vision.

## What is a Computer Vision System?
Details on the components and functioning of a computer vision system.

## Why Study Computer Vision?
- Useful in various fields such as personal photo albums, surveillance, security, movies, sports, medical and scientific imaging.
- 80% of all web traffic is images and videos.

## Computer Vision Applications
- Content-based image retrieval
- Face detection and tracking
- Face recognition
- Smile detection
- Biometrics (e.g., identifying individuals by iris patterns)

## Image Formation
- An image is a projection of a 3D scene into 2D.
- Composed of a grid of pixels, each with a fixed size.
- Pixels form the basic unit of an image.

## Cameras
- Evolution from pinhole cameras to modern lens-based cameras.
- Pinholes focus light rays but have limitations (e.g., blurring due to size).

## Sampling & Quantization
- Spatial sampling and amplitude quantization are fundamental processes in digital imaging.

## Data Structures for Image Analysis
- **Matrices:**
  - Common data structure for low-level image representation.
  - Used for binary images, grayscale images, and color images.
- **Histograms:**
  - Capture the distribution of gray levels in an image.
- **Co-occurrence Matrix:**
  - Describes how often pixels with specific intensities occur in spatial relationships.
- **Chains:**
  - Describe object borders (contours) and are useful for pattern matching.
- **Hierarchical Data Structures:**
  - **Pyramids:**
    - M-pyramid (Matrix Pyramid): Sequence of images with decreasing resolution.
    - T-pyramid (Tree Pyramid): Hierarchical data structure for image representation.
  - **Quad Trees:**
    - Modifications of T-pyramids with nodes having four children, useful for hierarchical image representation.

## Digital Image Properties
- **Pixel Adjacency:**
  - Takes into account spatial neighborhood and intensity groups.
