# https://adventofcode.com/2022/day/3

N = 3
IS = 'a'
OS = 'b'


with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
    total = 0

    group = []

    for line in f.readlines():
        line = set(line.strip())

        if len(group) < 2:
            group.append(line)

        else:
            shared = list(group[0].intersection(group[1]).intersection(line))[0]
            group = []

            # for lowercase subtract 96
            # for uppercase subtract 38

            if shared.islower():
                total += ord(shared) - 96
            else:
                total += ord(shared) - 38

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{total}')
