import numpy as np
import cv2

from enum import Enum

class ThresholdMethod(Enum):
    OPTIMAL = 1
    OTSU = 2
    SPECTRAL = 3

def histogram(image):
    rows, columns = image.shape
    frequency = np.zeros(256,dtype=int)
    for i in range(rows):
        for j in range(columns):
            frequency[image[i][j]] = frequency[image[i][j]] + 1
    return frequency

def cumlative_sum(frequency):
    cumlative = np.zeros(256,dtype=int)
    cumlative[0] = frequency[0]
    for i in range(1,256):
        cumlative[i] = cumlative[i-1] + frequency[i]
    return cumlative

def calc_variances(cum_mean,hist,cum_sum):
    variances = np.zeros((256, 1))
    for t in range(256):
        w0 = cum_mean[t]
        w1 = 1 - w0
        if w0 == 0 or w1 == 0:
            continue
        mu0 = np.sum(np.arange(0, t+1) * hist[0:t+1]) / cum_sum[t]
        mu1 = np.sum(np.arange(t+1, 256) * hist[t+1:256]) / (cum_sum[255] - cum_sum[t])
        variances[t] = w0 * w1 * (mu0 - mu1) ** 2
    return variances

def optimal_threshold(img):
    mean_value = np.mean(img)
    foreground = img[img >= mean_value]
    background = img[img < mean_value]

    mean_foreground = np.mean(foreground) if len(foreground) > 0 else 0
    mean_background = np.mean(background) if len(background) > 0 else 0

    optimal_threshold = int(round((mean_foreground + mean_background) / 2))
    return optimal_threshold


def otsu_threshold(img):
    # calculate histogram
    hist=histogram(img)
    # calculate cumlative sum of histogram
    cum_sum=cumlative_sum(hist)
    # calculate cumlative mean of histogram
    cum_mean = cum_sum / cum_sum[-1]
    # calculate variances
    variances = calc_variances(cum_mean,hist,cum_sum)
    # optimal threshold
    thres_value = np.argmax(variances)
    return thres_value

def spectral_thresholding_local(image, size):
    result = np.zeros(image.shape)
    i = 0
    j = 0
    nX = size[0]
    nY = size[1]
    while(j < image.shape[1]):
        i = 0
        nX = size[0]
        while(i < image.shape[0]):
            result[i:nX, j:nY] = spectral_thresholding(image[i:nX, j:nY])
            i = nX
            nX += size[0]
        j = nY
        nY += size[1]
    return result

def spectral_thresholding(img, k=10):

     # Convert the image to grayscale
    if len(img.shape) > 2:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img

    # Compute the histogram of the image
    hist = histogram(gray)

    # Compute the cumulative distribution function (CDF)
    cdf = cumlative_sum(hist)

    # Compute the normalized CDF
    cdf_normalized = cdf / float(cdf.max())

    # Calculate the mean of the entire image
    mean = np.sum(np.arange(256) * hist) / float(gray.size)

    # Initialize variables for the optimal threshold values and the maximum variance
    optimal_high = 0
    optimal_low = 0
    max_variance = 0

    # Loop over all possible threshold values, select ones with maximum variance between modes
    for high in range(0, 256):
        for low in range(0, high):
            w0 = np.sum(hist[0:low])
            if w0 == 0:
                continue
            mean0 = np.sum(np.arange(0, low) * hist[0:low]) / float(w0)

            # Calculate the weight and mean of the low pixels
            w1 = np.sum(hist[low:high])
            if w1 == 0:
                continue
            mean1 = np.sum(np.arange(low, high) * hist[low:high]) / float(w1)

            # Calculate the weight and mean of the high pixels
            w2 = np.sum(hist[high:])
            if w2 == 0:
                continue
            mean2 = np.sum(np.arange(high, 256) * hist[high:]) / float(w2)

            # Calculate the between-class variance
            variance = w0 * (mean0 - mean) * 2 + w1 * (mean1 - mean) * 2 + w2 * (mean2 - mean) ** 2

            # Update the optimal threshold values if the variance is greater than the maximum variance
            if variance > max_variance:
                max_variance = variance
                optimal_high = high
                optimal_low = low

    # Apply thresholding to the input image using the optimal threshold values
    binary = np.zeros(gray.shape, dtype=np.uint8)
    binary[gray < optimal_low] = 0
    binary[(gray >= optimal_low) & (gray < optimal_high)] = 128
    binary[gray >= optimal_high] = 255

    return binary

def global_threshold(imagePath, val_high=255, val_low=0, method=ThresholdMethod.OTSU):
    image = cv2.imread(imagePath,0)
    img = image.copy()
    thres_value=0

    if method == ThresholdMethod.OTSU:
        thres_value=otsu_threshold(image)

    elif method == ThresholdMethod.OPTIMAL:
        thres_value=optimal_threshold(image)

    elif method == ThresholdMethod.SPECTRAL:
        return spectral_thresholding(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > thres_value:
                img[i,j] = val_high
            else:
                img[i,j] = val_low
    
    cv2.imwrite("thresholding_output.png",img)

def local_threshold(imagePath, val_high, val_low,method=ThresholdMethod.OTSU,block_size = 3):
    image = cv2.imread(imagePath,0)
    img = image.copy()
    i=0 
    j=0 
    last_thresh_value = 127
    while i+block_size+1 < image.shape[0]:
        j=0
        while j+block_size + 1 < image.shape[1]:
            thresh_value=0

            img_block = image[[i,i+block_size]][:, [j,j+block_size]]
            if method == ThresholdMethod.OTSU:
                thresh_value=otsu_threshold(img_block)
            elif method == ThresholdMethod.OPTIMAL:
                thresh_value=optimal_threshold(img_block)
            elif method == ThresholdMethod.SPECTRAL:
                thresh_value= spectral_thresholding_local(img_block,block_size)
            else:
                return None
                
            last_thresh_value = thresh_value
            for k in range(i,i+block_size):
                for l in range(j,j+block_size):
                    if image[k,l] > thresh_value:
                        img[k,l] = val_high
                    else:
                        img[k,l] = val_low
            j+=block_size           
        i+=block_size
        
    for i in range(i,image.shape[0]):
        for j in range(j,image.shape[1]):
            if image[i,j] > last_thresh_value:
                img[i,j] = val_high
            else:
                img[i,j] = val_low

    cv2.imwrite("thresholding_output.png",img)
