# https://adventofcode.com/2022/day/4

N = 4
IS = 'a'
OS = 'a'

n_overlaps = 0

with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        p1, p2 = line.split(',')
        L1, U1 = map(int, p1.split('-'))
        L2, U2 = map(int, p2.split('-'))

        if ((L1 >= L2) and (U1 <= U2)) or ((L2 >= L1) and (U2 <= U1)):
            n_overlaps += 1

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{n_overlaps}')
