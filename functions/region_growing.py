import cv2
import numpy as np

def gray_diff(img, current_point, temp_point):
    return abs(int(img[current_point[0], current_point[1]]) - int(img[temp_point[0], temp_point[1]]))

def connects_selection(p):
    if p != 0:
        connects = [[-1, -1], [0, -1], [1, -1],[1, 0],[1, 1],[0, 1],[-1, 1],[-1, 0]]
    else:
        connects = [[0, -1], [1, 0],[0, 1], [-1, 0]]
    return connects

def region_growing_method(image_path, thresh,p = 5,seeds = [[25, 35],[88, 200],[30, 250]]):
    '''
    img: image array
    seeds: array of seed points
    thresh: threshold value
    p: 0 or 5, 0 for 4-connectivity and 5 for 8-connectivity
    '''
    img = cv2.imread(image_path)
    height, width = img.shape
    seed_mark = np.zeros(img.shape)
    seed_list = []
    for seed in seeds:
        seed_list.append(seed)
    label = 1
    connects = connects_selection(p)
    while(len(seed_list) > 0):
        current_pixel = seed_list.pop(0)
        seed_mark[current_pixel[0], current_pixel[1]] = label
        for i in range(8):
            tmpX = current_pixel[0] + connects[i][0]
            tmpY = current_pixel[1] + connects[i][1]
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= width:
                continue
            grayDiff = gray_diff(img, current_pixel, [tmpX, tmpY])
            if grayDiff < thresh and seed_mark[tmpX, tmpY] == 0:
                seed_mark[tmpX, tmpY] = label
                seed_list.append([tmpX, tmpY])
    
    cv2.imwrite("region_growing_output.png",seed_mark)
