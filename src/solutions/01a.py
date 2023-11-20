# https://adventofcode.com/2022/day/1

N = 1
IS = 'a'
OS = 'a'

best = 0

with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
    curr = 0

    for line in f.readlines():
        if (not line.strip()):
            if curr > best:
                best = curr
            curr = 0

        else:
            curr += int(line)

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{best}')
