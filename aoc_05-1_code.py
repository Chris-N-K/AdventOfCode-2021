import numpy as np

with open('./data/aoc_5_data.txt') as file:
    lines = file.readlines()

lines = [line.split(' -> ') for line in lines]
line_ends = []
for line in lines:
    l1, l2 = line
    c1 = tuple([int(i) for i in l1.split(',')])
    c2 = tuple([int(i) for i in l2.split(',')])
    line_ends.append((c1, c2))


def make_range_list(start, stop):
    if start > stop:
        step = -1
        stop -= 1
    elif start < stop:
        step = 1
        stop += 1
    else:
        return [start]
    return list(range(start, stop, step))


def make_line(nodes):
    start_node, end_node = nodes
    edge = [make_range_list(start_node[1], end_node[1]), make_range_list(start_node[0], end_node[0])]
    if len(edge[0]) != len(edge[1]):
        short = min(edge, key=len)
        edge[edge.index(short)] = [short[0] for i in max(edge, key=len)]
    return list(zip(*edge))


line_arr = np.zeros((1000,1000))

for le in line_ends:
    if le[0][0] == le[1][0] or le[0][1] == le[1][1]:
        for coord in make_line(le):
            line_arr[coord] += 1

print(len(line_arr[line_arr > 1]))
