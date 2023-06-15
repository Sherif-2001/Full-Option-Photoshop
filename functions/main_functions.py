import numpy as np
import cv2
from enum import Enum


class ThresholdMethod(Enum):
    OPTIMAL = 1
    OTSU = 2
    SPECTRAL = 3


def get_histogram(image):
    rows, columns = image.shape
    frequency = np.zeros(256,dtype=int)
    for i in range(rows):
        for j in range(columns):    
            frequency[image[i][j]] = list(frequency)[image[i][j]] + 1
    return frequency

def rgb_split(image):
    b_channel, g_channel, r_channel = cv2.split(image)
    return r_channel, g_channel, b_channel

#function for combining rgb channels into one image
def rgb_combine(r,g,b):
    image = cv2.merge((r,g,b))
    return image

#change from bgr to rgb
def BGR_to_RGB(image, cmap = "rgb"):
        r,g,b = rgb_split(image)
        image = rgb_combine(r,g,b)

#this function takes the RGB image and type of require conversion and returns a grayscale image
def rgb_to_grayscale(image, type = "UHDTV"):
    r,g,b = rgb_split(image)
    if type == "basic":
       return 1/3*(r+g+b) 
    if type == "NTSC":
        return 0.2989*r+0.5870*g+0.1140*b
    if type == "UHDTV":
        return 0.2627*r+0.6780*g+0.0593*b