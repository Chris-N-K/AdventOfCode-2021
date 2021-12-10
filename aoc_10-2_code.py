with open('./data/aoc_10_data.txt') as file:
    lines = [list(line.replace('\n', '')) for line in file.readlines()]

open_char = '([{<'
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
rpairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
cc_points = {')': 1, ']': 2, '}': 3, '>': 4}

rlines = []
for i, line in enumerate(lines):
    parsed = []
    corrupted = False
    while line:
        char = line.pop(0)
        if char in open_char:
            parsed.append(char)
        else:
            if parsed[-1] == pairs[char]:
                parsed.pop()
            else:
                corrupted = True
                break
    if not corrupted:
        cchars = reversed([rpairs[char] for char in parsed])
        rlines.append(cchars)

line_scores = []
for line in rlines:
    line_score = 0
    for char in line:
        line_score *= 5
        line_score += cc_points[char]
    line_scores.append(line_score)

sorted_scores = sorted(line_scores)
print(sorted_scores[len(sorted_scores)//2])
