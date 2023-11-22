# https://adventofcode.com/2022/day/4

N = 4
IS = 'a'
OS = 'b'

n_overlaps = 0

with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        p1, p2 = line.split(',')
        L1, U1 = map(int, p1.split('-'))
        L2, U2 = map(int, p2.split('-'))

        if any([
           L1 in range(L2, U2 + 1),
           L2 in range(L1, U1 + 1),
           U1 in range(L2, U2 + 1),
           U2 in range(L1, U1 + 1)
        ]):
            n_overlaps += 1

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{n_overlaps}')
