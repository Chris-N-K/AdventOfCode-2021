raw_input = open('./data/aoc_8_data.txt').readlines()
line_input = [line.replace('\n', '').split(' | ') for line in raw_input]
data = [(ref.split(' '), output.split(' ')) for (ref, output) in line_input]

test_ref = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
test_output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']


def make_ref_dict(stream):
    ref_d = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    for code in stream:
        if len(code) == 2:
            ref_d[1] = code
        elif len(code) == 4:
            ref_d[4] = code
        elif len(code) == 3:
            ref_d[7] = code
        elif len(code) == 7:
            ref_d[8] = code

    len6 = [code for code in stream if len(code) == 6]
    len5 = [code for code in stream if len(code) == 5]

    stop = 0
    while len6:
        code = len6.pop(0)
        if all([dc_l in code for dc_l in ref_d[4]]):
            ref_d[9] = code
        elif ref_d[9] != '' and all([dc_l in code for dc_l in ref_d[7]]):
            ref_d[0] = code
        elif not len6:
            ref_d[6] = code
        else:
            len6.append(code)
            stop += 1
            if stop == 10:
                print(ref_d)
                raise Exception()

    stop = 0
    while len5:
        code = len5.pop(0)
        if all([dc_l in code for dc_l in ref_d[7]]):
            ref_d[3] = code
        elif len(set(ref_d[6]).intersection(code)) == 5:
            ref_d[5] = code
        elif not len5:
            ref_d[2] = code
        else:
            len5.append(code)
            stop += 1
            if stop == 10:
                print(ref_d)
                raise Exception()
    return ref_d


def decode(ref_d, stream):
    clear_text = []
    for code in stream:
        for key, value in ref_d.items():
            if sorted(code) == sorted(value):
                clear_text.append((key, value, code))
    return clear_text


res = 0
for (input_sig, output_sig) in data:
    reference = make_ref_dict(input_sig)
    decoded = decode(reference, output_sig)
    print(decoded)
    res += int(''.join([str(i[0]) for i in decoded]))
print(res)
