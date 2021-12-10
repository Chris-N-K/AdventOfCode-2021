import numpy as np

with open("/home/cnk/AdventOfCode/3/aoc_3_data.txt") as file:
    data = file.readlines()

reformat_data = []
for i, line in enumerate(data):
    reformat_data.append([])
    for x in line:
        if x != '\n':
            reformat_data[i].append(int(x))

data = np.asarray(reformat_data)

gamma_bin = ''.join([str(np.argmax(np.bincount(data[:, i]))) for i in range(data.shape[1])])
epsilon_bin = ''.join(['0' if x == '1' else '1' for x in gamma_bin])
gamma = int(gamma_bin, 2)
epsilon = int(epsilon_bin, 2)
print('gamma', gamma_bin, gamma)
print('epsilon', epsilon_bin, epsilon)
print(gamma * epsilon)

