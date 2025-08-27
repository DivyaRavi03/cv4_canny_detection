# Project 04: Canny Edge Detection with OpenCV

This project implements the classic Canny Edge Detection algorithm using Python and OpenCV. It's a foundational technique in computer vision used to identify the structural outlines of objects in an image by detecting sharp changes in pixel intensity.

## Features

-   Loads an image from a local file.
-   Converts the image to grayscale, a necessary preprocessing step for the Canny algorithm.
-   Applies the Canny algorithm to produce a binary image showing the detected edges.
-   Displays the original image and the final edge map side-by-side for comparison.

## Technologies Used

-   Python
-   OpenCV
-   NumPy

## Theoretical Concepts

This project utilizes the `cv2.Canny()` function, which encapsulates the five core stages of the Canny algorithm:
1.  Noise Reduction (using a Gaussian filter)
2.  Gradient Intensity Calculation
3.  Non-Maximum Suppression
4.  Double Thresholding
5.  Hysteresis Edge Tracking
