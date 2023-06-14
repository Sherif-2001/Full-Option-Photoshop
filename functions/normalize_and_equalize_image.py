import numpy as np
from main_functions import get_histogram


def cumulative_sum(frequency):
    cumulative_sum_arr = frequency
    for i in range(1,frequency.size):
        cumulative_sum_arr[i] = cumulative_sum_arr[i] + cumulative_sum_arr[i-1]
    return cumulative_sum_arr

# --------------------------------- Histogram Equalization -------------------------------------
def equalization(image):
    cumulative = cumulative_sum(get_histogram(image))
    l = 256
    n = image.size
    rows,columns = image.shape
    equalized_image = np.zeros(image.shape,dtype=int)
    arr = np.zeros(256,dtype=int)
    for i in range(256):
        arr[i] = l / n * cumulative[i] - 1
    for i in range (rows):
        for j in range(columns):
           equalized_image[i][j] =  arr[image[i][j]]
        
    return equalized_image

# --------------------------------- Normalization -------------------------------------
def normalization(image):
    max_level = np.max(image)
    min_level = np.min(image)
    normalized_image = np.zeros(image.shape,dtype=int)
    rows,columns = image.shape
    for i in range(rows):
        for j in range(columns):
            normalized_image[i][j] = ((image[i][j] - min_level)/(max_level-min_level))*255
    
    return normalized_image
