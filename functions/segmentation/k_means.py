import numpy as np
from PIL import Image

def kmeans(array_im, k, limit_it):
    dim = array_im.shape[1]
    n = array_im.shape[0]
    it = 0
    rand = np.random.permutation(n)[:k]
    centres = array_im[rand,:]
    clusters = np.zeros(n)
    stop = False
    clusters_prev = clusters
    while not stop and it < limit_it:
        mean_K = np.zeros((k,dim))
        for i in range(n):
            d = np.zeros(k)
            for c in range(k):
                d[c] = np.sqrt((array_im[i,0] - centres[c,0])**2 + (array_im[i,1] - centres[c,1])**2 + (array_im[i,2] - centres[c,2])**2)
            clusterP = np.argmin(d)
            clusters[i] = clusterP
        for c in range(k):
            mean_K[c,:] = np.mean(array_im[clusters==c,:], axis=0)
        centres = mean_K
        if np.array_equal(clusters, clusters_prev):
            stop = True
        clusters_prev = clusters
        it += 1
    return clusters, centres


def K_means_segmentation(image_path, limit_it = 999999,k=8):

    image = Image.open(image_path)

    image = np.array(image)
    image = image.astype(np.float32) / 255.0

    arr = image.reshape(-1, 3)

    # KMEANS
    clusters, centres = kmeans(arr, k, limit_it)

    clusters = clusters.reshape((image.shape[0], image.shape[1]))

    centres = (centres*255.0).astype(np.uint8)
    final_image = np.zeros(image.shape, dtype=np.uint8)


    # Construct the image
    for i in range(clusters.shape[0]):
        for j in range(clusters.shape[1]):
            final_image[i,j,:] = centres[clusters[i,j].astype(int),:]

    Image.fromarray(final_image).save("K_means_output.png")
