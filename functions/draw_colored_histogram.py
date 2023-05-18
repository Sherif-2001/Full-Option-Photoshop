import cv2
from matplotlib import pyplot as plt
import numpy as np


def rgb_split(image):
    b_channel, g_channel, r_channel = cv2.split(image)
    return r_channel, g_channel, b_channel

#function for combining rgb channels into one image
def rgb_combine(r,g,b):
    image = cv2.merge((r,g,b))
    return image

#change from bgr to rgb
def show_img(image, cmap = "rgb"):
    if cmap == "rgb":
        r,g,b = rgb_split(image)
        image = rgb_combine(r,g,b)
        plt.imshow(image)
    else:
        plt.imshow(image,cmap="gray")

#this function takes the RGB image and type of require conversion and returns a grayscale image
def rgb_to_grayscale(image, type = "UHDTV"):
    r,g,b = rgb_split(image)
    if type == "basic":
       return 1/3*(r+g+b) 
    if type == "NTSC":
        return 0.2989*r+0.5870*g+0.1140*b
    if type == "UHDTV":
        return 0.2627*r+0.6780*g+0.0593*b
    
#generates histogram for the overall image RGB
def rgb_hist_cumulative(image):
    # calculate mean value from RGB channels and flatten to 1D array
    # vals = image.mean(axis=2).flatten()
    # get the rgb channels
    r_vals, g_vals, b_vals = rgb_split(image)
    r_hist = twoD_fast_hist(r_vals)
    g_hist = twoD_fast_hist(g_vals)
    b_hist = twoD_fast_hist(b_vals)
    fig, ax = plt.subplots(2,3)
    
    #plot r g b histograms
    ax[0,0].bar(np.arange(0,256),r_hist,color="red")
    ax[0,1].bar(np.arange(0,256),g_hist,color="green")
    ax[0,2].bar(np.arange(0,256),b_hist,color="blue")

    #plot r g b cumulatives
    ax[1,0].bar(np.arange(0,256),np.cumsum(r_hist),color="red")
    ax[1,1].bar(np.arange(0,256),np.cumsum(g_hist),color="green")
    ax[1,2].bar(np.arange(0,256),np.cumsum(b_hist),color="blue")

    plt.tight_layout()
    plt.savefig("static/assets/rgb_histogram_plot.png", bbox_inches='tight', pad_inches=0)

    
def twoD_fast_hist(matrix):
    # calculate histogram
    values = matrix.flatten()
    counts, bins = np.histogram(values, range(257))
    return counts