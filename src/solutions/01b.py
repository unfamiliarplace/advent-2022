# https://adventofcode.com/2022/day/1

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

best = []

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    curr = 0

    for line in f.readlines():
        if line.strip():
            curr += int(line)
        
        else:
            if len(best) < 3:
                best.append(curr)
            else:
                m = min(best)
                if (curr > m):
                    best.remove(m)
                    best.append(curr)
            curr = 0

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{sum(best)}')
