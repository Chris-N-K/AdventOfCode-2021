import numpy as np

with open('./data/aoc_11_data.txt') as file:
    earr = np.array([[int(i) for i in line if i != '\n'] for line in file.readlines()])

# earr = np.array([[1,1,1,1,1],[1,9,9,9,1],[1,9,1,9,1],[1,9,9,9,1],[1,1,1,1,1]])

class Dumbo:
    def __init__(self, energy, index, grid):
        self.grid = grid
        self.energy = energy
        self.index = index
        self.neighbors = self.get_neighbors()
        self.blocked = False
        self.flash_count = 0

    def __repr__(self):
        return str(self.energy)

    def get_neighbors(self):
        y, x = self.index
        raw_ind = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
        return [ind for ind in raw_ind if min(ind) >= 0 and ind[0] < self.grid.shape[0] and ind[1] < self.grid.shape[1]]

    def step(self):
        self.energy_increase()

    def reset(self):
        self.blocked = False

    def energy_increase(self):
        if not self.blocked:
            self.energy += 1
            self.flash()

    def flash(self):
        if self.energy > 9:
            self.blocked = True
            self.energy = 0
            self.flash_count += 1
            for ind in self.neighbors:
                self.grid[ind].energy_increase()


class Grid:
    def __init__(self, egrid):
        self.shape = egrid.shape
        self.array = self.init_array(egrid)

    def __repr__(self):
        return str(self.array)

    @staticmethod
    def fill_with_dumbo(energy, ind, grid):
        dumbo = Dumbo(energy=energy, index=ind, grid=grid)
        return dumbo

    def init_array(self, egrid):
        arr = np.empty(self.shape, dtype=object)
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                arr[y, x] = self.fill_with_dumbo(energy=egrid[y, x], ind=(y, x), grid=arr)
        return arr

    def step(self):
        energy_grid = np.zeros_like(self.array)
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                self.array[y, x].step()
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                energy_grid[y, x] = self.array[y, x].energy
                self.array[y, x].reset()
        return np.sum(energy_grid)


steps = 500
cave = Grid(earr)
for i in range(steps):
    total_energy = cave.step()
    if total_energy == 0:
        print(i+1)

res = 0
for dumbo in cave.array.flatten():
    res += dumbo.flash_count

print(res)
