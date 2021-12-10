import numpy as np


class Lanterfish:
    def __init__(self, init_counter=6):
        self.counter = init_counter
        self.child = None

    def __repr__(self):
        return str(self.counter)

    def birth(self):
        self.counter = 6
        self.child = Lanterfish(8)

    def new_day(self):
        if self.counter == 0:
            self.birth()
        else:
            self.counter -= 1


start = np.loadtxt('./data/aoc_6_data.txt', delimiter=',', dtype=int)
days = 80

fishes = [Lanterfish(i) for i in start]
#print(f'Initial: {fishes}')
for i in range(1, days + 1):
    new_born = []
    for fish in fishes:
        fish.new_day()
        if fish.child:
            new_born.append(fish.child)
            fish.child = None
    fishes.extend(new_born)
    #print(f'After {i} Days: {fishes}')

print(len(fishes))
