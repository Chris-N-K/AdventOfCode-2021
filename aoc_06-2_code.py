import numpy as np

# init
days = 10
start = np.loadtxt('./data/aoc_6_data.txt', dtype=int, delimiter=',')
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in start:
    fish[i] += 1

# first idea
for i in range(days):
    adults = list(fish[:7])
    children = list(fish[7:])
    birthing = adults.pop(0)
    fish = []
    while adults:
        fish.append(adults.pop(0))
    fish.append(birthing + children.pop(0))
    fish.append(children.pop(0))
    fish.append(birthing)

print(fish)
print(np.sum(fish))

# optimised
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in start:
    fish[i] += 1

for i in range(days):
    fish = list(fish[1:7]) + [int(fish[7]) + int(fish[0])] + [int(fish[8]), int(fish[0])]

print(fish)
print(sum(fish))
