import numpy as np
from skimage.segmentation import watershed

with open('./data/aoc_9_data.txt') as file:
    lines = file.readlines()
height_map = np.array([[int(i) for i in line if i != '\n'] for line in lines])

region_map = watershed(height_map)
lowest = [np.min(height_map[region_map == label]) for label in np.unique(region_map)]
risk_levels = [point + 1 for point in lowest]
print(sum(risk_levels))
