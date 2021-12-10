import numpy as np

with open('./data/aoc_4_data.txt') as file:
    num_stream = [int(i) for i in file.readline().split(',')]

cards = np.squeeze(np.split(np.loadtxt('./data/aoc_4_data.txt', skiprows=1, dtype=float).reshape((100, 5, 5)), 100))


def mask_num(card, num):
    card[card == num] = -0.1


def is_bingo(card):
    for i in range(5):
        row_zeros = np.sum(card[i, :])
        col_zeros = np.sum(card[:, i])
        if row_zeros < 0 or col_zeros < 0:
            return True
    return False


winning_num = None
winning_card = None
for num in num_stream:
    for card in cards:
        mask_num(card, num)
        if is_bingo(card) and not winning_num:
            print('Bingo!\n',
                  card)
            winning_num = num
            winning_card = np.copy(card)

all_unmarked = winning_card[winning_card != -0.1]
sum_unmarked = np.sum(all_unmarked)
res = sum_unmarked * winning_num

print(all_unmarked)
print(sum_unmarked)
print(res)
