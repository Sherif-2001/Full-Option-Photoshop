import numpy as np
from functions.main_functions import get_histogram,rgb_to_grayscale,ThresholdMethod

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
    hist = get_histogram(img)

    # calculate cumlative sum of histogram
    cum_sum = cumlative_sum(hist)

    # calculate cumlative mean of histogram
    cum_mean = cum_sum / cum_sum[-1]

    # calculate variances
    variances = calc_variances(cum_mean, hist, cum_sum)

    # optimal threshold
    thres_value = np.argmax(variances)
    return thres_value


def spectral_thresholding(img, k=10):

    # Convert the image to grayscale
    if len(img.shape) > 2:
        gray = rgb_to_grayscale(img)
    else:
        gray = img

    # Compute the histogram of the image
    hist = get_histogram(gray)

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


# def spectral_thresholding_local(image, size):
#     result = np.zeros(image.shape)
#     i, j = 0, 0 
#     nX = size[0]
#     nY = size[1]
#     while(j < image.shape[1]):
#         i = 0
#         nX = size[0]
#         while(i < image.shape[0]):
#             result[i:nX, j:nY] = spectral_thresholding(image[i:nX, j:nY])
#             i = nX
#             nX += size[0]
#         j = nY
#         nY += size[1]
#     return result


def global_threshold(image, val_high=255, val_low=0, method=ThresholdMethod.OTSU):
    img = image.copy()
    image = rgb_to_grayscale(image)
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
    
    return img

def local_threshold(image, val_high=255, val_low=0,method = ThresholdMethod.OTSU,block_size = 3):
    img = image.copy()
    image = rgb_to_grayscale(image)
    i, j = 0, 0 
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
                # Check if the spectral_thresholding_local is right?
                # thresh_value= spectral_thresholding_local(img_block)
                thresh_value= spectral_thresholding(img_block)
                
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

    return img
