
import cv2
import numpy as np

from functions.edge_detection_filters import sobel_edge_detection
from functions.noise_filters import gaussian_filter
from functions.normalize_and_equalize_image import normalization


def harris_corner_detection(imagePath, alpha = 0.04, threshold = 0.6):
    image = cv2.imread(imagePath)
    image_copy = image.copy()
    image_gray = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)

    # Detect edges using sobel to get the derivatives
    Ix, Iy = sobel_edge_detection(image_gray)
    
    # Squaring the derivatives and cross multiplication
    Ixx = np.square(Ix) 
    Iyy = np.square(Iy)
    Ixy = Ix * Iy

    # Filter the derivatives using Gaussian filter
    Ixx_gauss = gaussian_filter(Ixx)
    Iyy_gauss = gaussian_filter(Iyy)
    Ixy_gauss = gaussian_filter(Ixy)

    # Cornerness Function
    det = Ixx_gauss * Iyy_gauss - np.square(Ixy_gauss)
    trace = Ixx_gauss + Iyy_gauss
    R =  det - alpha * np.square(trace)

    # Normalize
    R = normalization(R)

    # find all points above threshold (non-maximum supression line)
    loc = np.where(R >= threshold)
    for corner in zip(*loc[::-1]):
        cv2.circle(image_copy, corner, 15,(0,0,255))

    cv2.imwrite("harris_output.png",image_copy)