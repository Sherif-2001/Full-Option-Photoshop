import random
import numpy as np


def salt_pepper_noise(image, prob = 0.05):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    noisy_image = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noisy_image[i][j] = 0
            elif rdn > thres:
                noisy_image[i][j] = 255
            else:
                noisy_image[i][j] = image[i][j]
    return noisy_image

def gaussian_noise(image, mean=0, std=0.1):
    noise = np.multiply(np.random.normal(mean, std, image.shape), 255)
    noisy_image = np.clip(image.astype(int)+noise, 0, 255)
    return noisy_image

def uniform_noise(image, prob=0.1):
    levels = int((prob * 255) // 2)
    noise = np.random.uniform(-levels, levels, image.shape)
    noisy_image = np.clip(image.astype(int) + noise, 0, 255)
    return noisy_image