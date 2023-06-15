from matplotlib import pyplot as plt
import numpy as np
from functions.main_functions import rgb_split

def twoD_fast_hist(matrix):
    # calculate histogram
    values = matrix.flatten()
    counts, bins = np.histogram(values, range(257))
    return counts

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
    
    #plot rgb histograms
    ax[0,0].bar(np.arange(0,256),r_hist,color="red")
    ax[0,1].bar(np.arange(0,256),g_hist,color="green")
    ax[0,2].bar(np.arange(0,256),b_hist,color="blue")

    #plot rgb cumulatives
    ax[1,0].bar(np.arange(0,256),np.cumsum(r_hist),color="red")
    ax[1,1].bar(np.arange(0,256),np.cumsum(g_hist),color="green")
    ax[1,2].bar(np.arange(0,256),np.cumsum(b_hist),color="blue")

    plt.tight_layout()
    plt.savefig("static/assets/rgb_histogram_plot.png", bbox_inches='tight', pad_inches=0)