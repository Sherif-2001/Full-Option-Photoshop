import numpy as np
from functions.filters.edge_detection_filters import canny_edge_detection

def hough_line(image,edge):
    image = canny_edge_detection(image)
    row,column = edge.shape
    max_normal = int(np.round(np.sqrt(row**2 + column**2)))
    thetas = np.deg2rad(np.arange(-90, 91))
    r = np.arange(0,max_normal+1)
    accumulator = np.zeros((len(r), len(thetas)))
    for y in range(row):
        for x in range(column):
            if edge[y,x] > 0:
                for k in range(len(thetas)):
                    normal = x * np.cos(thetas[k]) + y * np.sin(thetas[k])
                    accumulator[int(normal),k] += 1

    for i in range(accumulator.shape[0]): # i is radius
        for j in range(accumulator.shape[1]): # j is theta
            if(accumulator[i][j] >= 150): # this is line
                if(int(thetas[j])==0):
                    if(r[i] < image.shape[1]):
                        x = r[i]
                        for k in range(image.shape[0]):
                            image[k][x] = 0
                else:
                    for k in range(image.shape[1]):
                        x = k
                        y = (-1 * np.cos(thetas[j]) / np.sin(thetas[j]) * x) + (r[i] / np.sin(thetas[j]))
                        if(y >= 0 and y < image.shape[0]):
                            image[int(y)][x] = 0
    return image 


def hough_circle(image,edge):
    image = canny_edge_detection(image)
    row,column = edge.shape
    max_radius = int(np.round(np.sqrt(row**2 + column**2)))
    accumulator = np.zeros((row,column,max_radius))

    for r in range(0,max_radius):
        for y in range(row):
            for x in range(column):
                if(edge[y,x] > 0):
                    for theta in range(0,361):
                        a = x - r * np.cos(theta * np.pi / 180)
                        b = y - r * np.sin(theta * np.pi / 180)
                        if(a >= 0 and a < column and b >= 0 and b < row):
                            accumulator[int(b)][int(a)][r] += 1

    for b in range(row):
        for a in range(column):
            for r in range(max_radius):
                if(accumulator[b][a][r] >= 200):
                    for x in range(image.shape[1]):
                        temp = r**2 - (x - a)**2
                        if(temp >= 0):
                            y_positive = int(np.sqrt(temp) + b) 
                            y_negative = int(-1 * np.sqrt(temp) + b) 
                            if(y_positive >= 0 and y_positive < image.shape[0] and y_negative >= 0 and y_negative < image.shape[0]):
                                image[y_positive][x] = 0
                                image[y_negative][x] = 0
    return image