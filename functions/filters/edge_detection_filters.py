import numpy as np
import scipy.signal as sig
import cv2

from filters.noise_filters import gaussian_filter

def canny_edge_detection(image, weak_th = None, strong_th = None):
# defining the canny detector function 
# weak_th and strong_th are thresholds for double thresholding step
       
    # Noise reduction step
    image = gaussian_filter(image)

    # Calculating the gradients
    gx = cv2.Sobel(np.float32(image), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(image), cv2.CV_64F, 0, 1, 3)
      
    # Conversion of Cartesian coordinates to polar 
    magnitude, ang = cv2.cartToPolar(gx, gy, angleInDegrees = True)
       
    # setting the minimum and maximum thresholds 
    # for double thresholding
    mag_max = np.max(magnitude)
    if not weak_th:weak_th = mag_max * 0.1
    if not strong_th:strong_th = mag_max * 0.5
      
    # getting the dimensions of the input image  
    height, width = image.shape
       
    # Looping through every pixel of the grayscale 
    # image
    for i_x in range(width):
        for i_y in range(height):
               
            grad_ang = ang[i_y, i_x]
            grad_ang = abs(grad_ang-180) if abs(grad_ang)>180 else abs(grad_ang)
               
            # selecting the neighbours of the target pixel
            # according to the gradient direction
            # In the x axis direction
            if grad_ang<= 22.5:
                neighb_1_x, neighb_1_y = i_x-1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
              
            # top right (diagonal-1) direction
            elif grad_ang>22.5 and grad_ang<=(22.5 + 45):
                neighb_1_x, neighb_1_y = i_x-1, i_y-1
                neighb_2_x, neighb_2_y = i_x + 1, i_y + 1
              
            # In y-axis direction
            elif grad_ang>(22.5 + 45) and grad_ang<=(22.5 + 90):
                neighb_1_x, neighb_1_y = i_x, i_y-1
                neighb_2_x, neighb_2_y = i_x, i_y + 1
              
            # top left (diagonal-2) direction
            elif grad_ang>(22.5 + 90) and grad_ang<=(22.5 + 135):
                neighb_1_x, neighb_1_y = i_x-1, i_y + 1
                neighb_2_x, neighb_2_y = i_x + 1, i_y-1
              
            # Now it restarts the cycle
            elif grad_ang>(22.5 + 135) and grad_ang<=(22.5 + 180):
                neighb_1_x, neighb_1_y = i_x-1, i_y
                neighb_2_x, neighb_2_y = i_x + 1, i_y
               
            # Non-maximum suppression step
            if width>neighb_1_x>= 0 and height>neighb_1_y>= 0:
                if magnitude[i_y, i_x]<magnitude[neighb_1_y, neighb_1_x]:
                    magnitude[i_y, i_x]= 0
                    continue
   
            if width>neighb_2_x>= 0 and height>neighb_2_y>= 0:
                if magnitude[i_y, i_x]<magnitude[neighb_2_y, neighb_2_x]:
                    magnitude[i_y, i_x]= 0
   
    ids = np.zeros_like(image)
       
    # double thresholding
    for i_x in range(width):
        for i_y in range(height):
              
            grad_mag = magnitude[i_y, i_x]
              
            if grad_mag<weak_th:
                magnitude[i_y, i_x]= 0
            elif strong_th>grad_mag>= weak_th:
                ids[i_y, i_x]= 1
            else:
                ids[i_y, i_x]= 2

    return magnitude

def prewitt_edge_detection(image):
    maskX = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    maskY = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

    prewittx = sig.convolve2d(image, maskX)
    prewitty = sig.convolve2d(image, maskY)
    edge_image = np.add(prewittx, prewitty)
    return edge_image

def roberts_edge_detection(image):
    maskX = np.array([[0,1],[-1,0]])
    maskY = np.array([[1,0],[0,-1]])

    image = image.astype(np.float64)
    image /= 255.0

    robertsx = sig.convolve2d(image, maskX)
    robertsy = sig.convolve2d(image, maskY)

    edge_image = np.add(robertsx ,robertsy)
    edge_image *= 255

    return edge_image

def sobel_edge_detection(image):
    maskX = [[1, 0, -1],
             [2, 0, -2],
             [1, 0, -1]]
    
    maskY = [[1, 2, 1],
             [0, 0, 0],
             [-1, -2, -1]]
    
    sobelX = sig.convolve2d(image, maskX)
    sobelY = sig.convolve2d(image, maskY )
    edge_image = np.add(sobelX,sobelY)
    
    return edge_image
