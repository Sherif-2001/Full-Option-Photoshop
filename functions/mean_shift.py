from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

bandwidth = 2
Bin = 40

def gaussian_mean(kernel, seed, bandwidth):
    # Apply Gaussian kernel to the seed point using the given bandwidth
    kernel = gaussian_filter(kernel, sigma=bandwidth)

    # Compute the weighted sum of the kernel and the color values of the pixels
    # in the region defined by the kernel
    if kernel.size > 0:
        mean = np.sum(kernel * seed, axis=0) / np.sum(kernel)
    else:
        mean = seed

    return mean

def mean_shift_method(image_path, num_samples = 5, threshold = 1.0,m = 1):

    img = Image.open(image_path)
    img.load()
    img = np.array(img)

    seg_img = img

    rows, cols, dim = img.shape

    meandist = np.array([[1000.0 for r in range(cols)] for c in range(rows)])
    labels = np.zeros((rows, cols), dtype=np.int32)


    means = []
    for r in range(0,rows,Bin):
        for c in range(0,cols,Bin):
            seed = np.array([r,c,img[r][c][0],img[r][c][1],img[r][c][2]])
            for n in range(15):
                x = seed[0]
                y = seed[1]
                r1 = max(0,x-Bin)
                r2 = min(r1+Bin*2, rows)
                c1 = max(0,y-Bin)
                c2 = min(c1+Bin*2, cols)
                kernel = []
                for i in range(int(r1), int(r2)):
                    for j in range(int(c1), int(c2)):
                        dc = np.linalg.norm(img[i][j] - seed[2:])
                        ds = (np.linalg.norm(np.array([i,j]) - seed[:2]))*m/num_samples
                        D = np.linalg.norm([dc,ds])
                        if D < bandwidth:
                            kernel.append([i,j,img[i][j][0],img[i][j][1],img[i][j][2]])
                kernel = np.array(kernel)			
                mean = gaussian_mean(kernel, seed, bandwidth)
                # Get the shift
                dc = np.linalg.norm(seed[2:] - mean[2:])
                ds = (np.linalg.norm(seed[:2] - mean[:2]))*m/num_samples
                dsm = np.linalg.norm([dc,ds])
                seed = mean
                if dsm <= threshold:
                    # print "Mean " + str(len(means)+1) + " converges in: " + str(n) + " iterations"
                    break
            means.append(seed)



    # Grouping together the means that are closer than the bandwidth
    flags = [1 for me in means]
    for i in range(len(means)):
        if flags[i] == 1:
            w = 1.0
            j = i + 1
            while j < len(means):
                dc = np.linalg.norm(means[i][2:] - means[j][2:])
                ds = (np.linalg.norm(means[i][:2] - means[j][:2]))*m/num_samples
                dsm = np.linalg.norm([dc,ds])
                if dsm < bandwidth:
                    means[i] = means[i] + means[j]
                    w = w + 1.0
                    flags[j] = 0
                j = j + 1
            means[i] = means[i]/w
    converged_means = []
    for i in range(len(means)):
        if flags[i] == 1:
            converged_means.append(means[i])
    converged_means = np.array(converged_means)

    # Constructing the segmented image
    for i in range(rows):
            for j in range(cols):
                    for c in range(len(converged_means)):
                            dc = np.linalg.norm(img[i][j] - converged_means[c][2:])
                            ds = (np.linalg.norm(np.array([i,j]) - converged_means[c][:2]))*m/num_samples
                            D = np.linalg.norm([dc,ds])
                            if D < meandist[i][j]:
                                    meandist[i][j] = D
                                    labels[i][j] = c
                    seg_img[i][j] = converged_means[labels[i][j]][2:]

    seg_img = Image.fromarray(seg_img)
    seg_img.save("mean_shift_output.png")
