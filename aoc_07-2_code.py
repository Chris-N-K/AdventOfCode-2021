import numpy as np

testdata = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
data = np.loadtxt('./data/aoc_7_data.txt', delimiter=',', dtype=int)


def fuel_increase(s_count):
    fuel = 0
    factor = 1
    for s in range(s_count):
        fuel += factor
        factor += 1
    return fuel


def search_optimal(start_positions, window=100):
    pos_optimal_pos = int(np.round(np.mean(start_positions)))
    pos_end_positions = [i for i in range(pos_optimal_pos - window, pos_optimal_pos)] + [pos_optimal_pos, pos_optimal_pos + window]
    fc_rates = {}
    for end_pos in pos_end_positions:
        steps = [int(abs(start - end_pos)) for start in start_positions]
        fuel_consumption = [fuel_increase(s) for s in steps]
        fc_rates[end_pos] = np.sum(fuel_consumption)
    return fc_rates


fuel_consumption_rates = search_optimal(data)
print(fuel_consumption_rates)
min_fuel = min(fuel_consumption_rates.values())
print(list(fuel_consumption_rates.keys())[list(fuel_consumption_rates.values()).index(min_fuel)], min_fuel)

# alternative way to find the optimal position?
print(int(np.mean(data)))
