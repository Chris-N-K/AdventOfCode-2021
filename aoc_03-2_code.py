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


def find_feature_code(inarr, pos, mode):
    bincount = np.bincount(inarr[:, pos])
    if mode=='max':
        if bincount[0] == bincount[1]:
            x = 1
        else:
            x = np.argmax(bincount)
    elif mode=='min':
        if bincount[0] == bincount[1]:
            x = 0
        else:
            x = np.argmin(bincount)
    index = np.where(inarr[:, pos] == x)[0]
    return np.array([inarr[ind, :] for ind in index])

i = 0
oxygen = data
while oxygen.shape[0] > 1:
    oxygen = find_feature_code(oxygen, i, 'max')
    i += 1
oxygen = np.squeeze(oxygen)

i = 0
co2 = data
while co2.shape[0] > 1:
    co2 = find_feature_code(co2, i, 'min')
    i += 1
co2 = np.squeeze(co2)

oxy_bin = ''.join([str(x) for x in oxygen])
co2_bin = ''.join([str(x) for x in co2])
oxy_num = int(oxy_bin, 2)
co2_num = int(co2_bin, 2)

print('oxygen', oxy_bin, oxy_num)
print('co2', co2_bin, co2_num)
print(oxy_num * co2_num)

