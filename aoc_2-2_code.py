# load data
with open("/home/cnk/AdventOfCode/2/aoc_2_data.txt") as file:
    commands = file.readlines()

h_pos = 0
v_pos = 0
aim = 0

for command in commands:
    direction, count = command.split(' ')
    if direction == 'down':
        aim += int(count)
    elif direction == 'up':
        aim -= int(count)
    else:
        h_pos += int(count)
        v_pos += aim * int(count)

print('h_pos', h_pos)
print('v_pos', v_pos)
print('res', h_pos * v_pos)
