import numpy as np

# load data
data = np.loadtxt('/home/cnk/AdventOfCode/1/aoc_1_data.txt')

last = None
increase = 0
equal = 0
decrease = 0

for i in data:
    if last and i > last:
        increase += 1
    elif last and i == last:
        equal += 1
    elif last and i < last:
        decrease += 1
    last = i

print('increase', increase)
print('equal', equal)
print('decrease', decrease)
