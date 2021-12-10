raw_input = open('./data/aoc_8_data.txt').readlines()
line_input = [line.replace('\n', '').split(' | ') for line in raw_input]
data = [(ref.split(' '), output.split(' ')) for (ref, output) in line_input]

counter = 0
for (ref, output) in data:
    for i in output:
        if len(i) in [2, 3, 4, 7]:
            counter += 1
print(counter)
