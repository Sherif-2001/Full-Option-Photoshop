# --------------------------------- Global Thresholding -------------------------------------
def global_threshold(image, val_low = 0, val_high = 255, thres_value = 127):
    new_image = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > thres_value:
                new_image[i,j] = val_high
            else:
                new_image[i,j] = val_low
    return new_image

# --------------------------------- Local Thresholding -------------------------------------

def calculate_mean(rowStartIndex, rowEndIndex, colStartIndex, colEndIndex, image):
    sum = 0
    for i in range(rowStartIndex,rowEndIndex):
        for j in range(colStartIndex,colEndIndex):
            sum += image[i,j]
    return sum/((rowEndIndex-rowStartIndex)*(colEndIndex-colStartIndex))

def local_threshold(image, val_low = 0, val_high = 255, block_size = 5):
    new_image = image.copy()
    i=0 
    j=0 
    lastMean = 127
    while i+block_size-1 < image.shape[0]:
        j=0
        while j+block_size-1 < image.shape[1]:
            mean=calculate_mean(i,i+block_size,j,j+block_size,image)
            lastMean = mean
            for k in range(i,i+block_size):
                for l in range(j,j+block_size):
                    if image[k,l] > mean:
                        new_image[k,l] = val_high
                    else:
                        new_image[k,l] = val_low
            j+=block_size           
        i+=block_size
        
    for i in range(i,image.shape[0]):
        for j in range(j,image.shape[1]):
            if image[i,j] > lastMean:
                new_image[i,j] = val_high
            else:
                new_image[i,j] = val_low
    return new_image
