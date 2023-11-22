# https://adventofcode.com/2022/day/1

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

best = 0

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    curr = 0

    for line in f.readlines():
        if (not line.strip()):
            if curr > best:
                best = curr
            curr = 0

        else:
            curr += int(line)

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{best}')
