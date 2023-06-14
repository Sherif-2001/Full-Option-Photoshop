from enum import Enum
import numpy as np
from PIL import Image

class DistanceCalculation(Enum):
    Min = 1
    Euclidean = 2

class cluster_node:
    def __init__(self, vec, id, left=None, right=None, distance=0.0, node_vector=None):
        self.leftnode = left
        self.rightnode = right
        self.vec = vec
        self.id = id
        self.distance = distance
        if node_vector is None:
            self.node_vector = [self.id]
        else:
            self.node_vector = node_vector[:]

def euclidean_distance(vec1, vec2):
    return np.sqrt(sum((vec1 - vec2) ** 2))

def min_distance(clust1, clust2, distances):
    d = 1e12
    for i in clust1.node_vector:
        for j in clust2.node_vector:
            try:
                distance = distances[(i,j)]
            except:
                try:
                    distance = distances[(j,i)]
                except:
                    distance = euclidean_distance(clust1.vec, clust2.vec)
            if distance < d:
                d = distance
    return d

def agglomerative_clustering(input_path, distance = DistanceCalculation.Min, k = 40):
    image = np.array(Image.open(input_path))
    
    # cluster the pixels of the image
    distances = {}
    currentclustid = -1
    
    # cluster nodes are initially just the individual pixels
    nodes = [cluster_node(np.array(image[i,j,:]), id=i*image.shape[1]+j) for i in range(image.shape[0]) for j in range(image.shape[1])]
    
    while len(nodes) > k:
        lowestpair = (0,1)
        closest = euclidean_distance(nodes[0].vec,nodes[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(nodes)):
            for j in range(i+1,len(nodes)):
                # distances is the cache of distance calculations
                if (nodes[i].id,nodes[j].id) not in distances:
                    if distance == DistanceCalculation.Min:
                        distances[(nodes[i].id,nodes[j].id)] = min_distance(nodes[i], nodes[j], distances)
                    elif distance == DistanceCalculation.Euclidean:
                        distances[(nodes[i].id,nodes[j].id)] = euclidean_distance(nodes[i].vec,nodes[j].vec)

                d = distances[(nodes[i].id,nodes[j].id)]

                if d < closest:
                    closest = d
                    lowestpair = (i,j)
      
        # calculate the average of the two nodes
        len0 = len(nodes[lowestpair[0]].node_vector)
        len1 = len(nodes[lowestpair[1]].node_vector)
        mean_vector = [(len0*nodes[lowestpair[0]].vec[i] + len1*nodes[lowestpair[1]].vec[i])/(len0 + len1) \
                        for i in range(len(nodes[0].vec))]

        # create the new cluster node
        new_node = cluster_node(np.array(mean_vector), currentclustid, left=nodes[lowestpair[0]], right=nodes[lowestpair[1]], \
            distance=closest, node_vector=nodes[lowestpair[0]].node_vector + nodes[lowestpair[1]].node_vector)

        # cluster ids that weren't in the original set are negative
        currentclustid -= 1
        del nodes[lowestpair[1]]
        del nodes[lowestpair[0]]
        nodes.append(new_node)

    # create a new image array with the same shape as the original image
    new_image = np.zeros_like(image)

    # assign each pixel in the new image to its corresponding cluster
    for i in range(len(nodes)):
        for j in nodes[i].node_vector:
            row = j // image.shape[1]
            col = j % image.shape[1]
            new_image[row, col, :] = nodes[i].vec

    
    # convert the image array to a PIL image object
    img = Image.fromarray(np.uint8(new_image))

    # save the image to the output path
    img.save('agglomerative_output.png')