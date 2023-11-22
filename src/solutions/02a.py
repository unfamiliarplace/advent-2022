# https://adventofcode.com/2022/day/2

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

shapes = {
    'X': [
        1,
        {
            'A': 3,
            'B': 0,
            'C': 6
        }],
    'Y': [
        2,
        {
            'A': 6,
            'B': 3,
            'C': 0
        }],
    'Z': [
        3,
        {
            'A': 0,
            'B': 6,
            'C': 3
        }]
}

score = 0

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        opp, plr = line.split()

        score += shapes[plr][0]
        score += shapes[plr][1][opp]

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{score}')
