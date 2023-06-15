import numpy as np
import scipy.signal as sig
from functions.main_functions import rgb_to_grayscale

def average_filter(image, maskSize = [3,3]):
    
    # Make average filter mask
    mask = np.ones(maskSize, dtype = int)
    mask = mask / sum(sum(mask))

    # Convolve the image and the mask
    filtered_image = sig.convolve2d(rgb_to_grayscale(image), mask, mode="same")
    return filtered_image

def gaussian_filter(image, mask_size = 3,sigma = 1):
    if len(image.shape) > 2:
        image = rgb_to_grayscale(image)

    # Make gaussian filter mask using gaussian function
    p1 = 1/(2*np.pi*sigma**2)
    p3 = (2*np.square(sigma))
    mask = np.fromfunction(lambda x, y: p1 * np.exp(-(np.square(x-(mask_size-1)/2) + np.square(y-(mask_size-1)/2)) / p3), (mask_size, mask_size))
    mask = mask/np.sum(mask)

    # Convolve the image and the mask
    filtered_image = sig.convolve2d(image, mask, mode="same")
    return filtered_image

def median_filter(image, filter_size = 3):
    image = rgb_to_grayscale(image)
    row, col = image.shape
    filtered_image = np.zeros([row,col])
    filter_index = filter_size // 2

    for row_index in range(row):
        for column_index in range(col):
            temp = []
            for z in range(filter_size):
                if row_index + z - filter_index < 0 or row_index + z - filter_index > row - 1:
                    for _ in range(filter_size):
                        temp.append(0)
                elif column_index + z - filter_index < 0 or column_index + filter_index > col - 1:
                    temp.append(0)
                else:
                    for k in range(filter_size):
                        temp.append(image[row_index + z - filter_index][column_index + k - filter_index])

            temp.sort()
            filtered_image[row_index][column_index] = temp[len(temp) // 2]
    return filtered_image