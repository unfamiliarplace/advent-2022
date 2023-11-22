# https://adventofcode.com/2022/day/3

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

total = 0

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        
        n = len(line)
        p1, p2 = line[:n//2], line[n//2:]
        s1, s2 = set(p1), set(p2)
        shared = list(s1.intersection(s2))[0]

        # for lowercase subtract 96
        # for uppercase subtract 38

        if shared.islower():
            total += ord(shared) - 96
        else:
            total += ord(shared) - 38

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{total}')
