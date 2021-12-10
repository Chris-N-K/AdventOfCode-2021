import numpy as np

with open('./data/aoc_10_data.txt') as file:
    lines = [list(line.replace('\n', '')) for line in file.readlines()]

open_char = '([{<'
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
ind = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2, '<': 3, '>': 3}
e_points = np.array([3, 57, 1197, 25137])

illegal = [0, 0, 0, 0]
for i, line in enumerate(lines):
    parsed = []
    while line:
        char = line.pop(0)
        if char in open_char:
            parsed.append(char)
        else:
            if parsed[-1] == pairs[char]:
                parsed.pop()
            else:
                print(f'line {i+1}')
                illegal[ind[char]] += 1
                break

print(np.sum(e_points * illegal))

