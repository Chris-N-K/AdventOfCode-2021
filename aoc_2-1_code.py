# load data
with open("/home/cnk/AdventOfCode/2/aoc_2_data.txt") as file:
    commands = file.readlines()

h_pos = 0
v_pos = 0

for command in commands:
    print(command)
    direction, count = command.split(' ')
    if direction == 'forward':
        h_pos += int(count)
    elif direction == 'down':
        v_pos += int(count)
    else:
        v_pos -= int(count)

print('h_pos', h_pos)
print('v_pos', v_pos)
print('res', h_pos * v_pos)
