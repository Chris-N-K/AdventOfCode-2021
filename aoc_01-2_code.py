import numpy as np

# load data
data = np.loadtxt('/home/cnk/AdventOfCode/1/aoc_1_data.txt')

last = None
increase = 0
equal = 0
decrease = 0

for i in range(1, len(data)):
    window = data[i-1:i+2]
    wsum = np.sum(window)
    if last and wsum > last:
        increase += 1
    elif last and wsum == last:
        equal += 1
    elif last and wsum < last:
        decrease += 1
    last = wsum

print('increase', increase)
print('equal', equal)
print('decrease', decrease)
