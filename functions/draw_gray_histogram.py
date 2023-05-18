from matplotlib import pyplot as plt
import numpy as np


def histogram(image):
    rows, columns = image.shape
    frequency = np.zeros(256,dtype=int)
    for i in range(rows):
        for j in range(columns):
            frequency[image[i][j]] = frequency[image[i][j]] + 1
    return frequency

def saveHistogramPlot(image):
    plt.figure()
    plt.plot(histogram(image))
    plt.savefig("static/assets/histogram_plot.png", bbox_inches='tight', pad_inches=0)
