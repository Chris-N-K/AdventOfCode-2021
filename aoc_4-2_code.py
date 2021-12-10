import numpy as np

with open('./data/aoc_4_data.txt') as file:
    num_stream = [int(i) for i in file.readline().split(',')]

cards = [np.squeeze(i) for i in np.split(np.loadtxt('./data/aoc_4_data.txt', skiprows=1, dtype=float).reshape((100, 5, 5)), 100)]


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

while num_stream:
    bingo_cards = set()
    if len(cards) == 1:
        break
    num = num_stream.pop(0)
    ind = 0

    for i, card in enumerate(cards):
        mask_num(card, num)
        if is_bingo(card):
            bingo_cards.add(i)

    new_cards = [card for i, card in enumerate(cards) if not i in bingo_cards]
    cards = new_cards

while num_stream:
    num = num_stream.pop(0)
    mask_num(cards[0], num)
    if is_bingo(cards[0]):
        break

print(cards[0])
print(np.sum(cards[0][cards[0] != -0.1]))
print(num)
print(np.sum(cards[0][cards[0] != -0.1]) * num)