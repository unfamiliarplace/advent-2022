# https://adventofcode.com/2022/day/6

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

result = 0

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    chars = f.readline()
    for i in range(3, len(chars)):
        s = set(chars[i - 3:i + 1])
        if len(s) == 4:
            result = i + 1
            break

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{result}')
