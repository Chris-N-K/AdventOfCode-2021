import numpy as np
from skimage.segmentation import watershed

with open('./data/aoc_9_data.txt') as file:
    lines = file.readlines()
hight_map = np.array([[int(i) for i in line if i != '\n'] for line in lines])

region_map = watershed(hight_map)
region_map[hight_map == 9] = 0
region_sizes = [len(region_map[region_map == label]) for label in np.unique(region_map) if label != 0]
print(hight_map)
print(region_map)
print(region_sizes)
three_largest = sorted(region_sizes)[-3:]
print(three_largest)
print(three_largest[0] * three_largest[1] * three_largest[2])