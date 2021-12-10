import numpy as np

testdata = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
data = np.loadtxt('./data/aoc_7_data.txt', delimiter=',', dtype=int)

optimal_pos = np.round(np.median(data))
fuel_consumption = [abs(start - optimal_pos) for start in data]
print(np.sum(fuel_consumption))
