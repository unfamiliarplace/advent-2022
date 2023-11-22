# https://adventofcode.com/2022/day/5

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

stacks = []
moves = []

def parse(f):
    state = 0
    done_first = False

    for line in f.readlines():
            line = line.strip('\n')

            if state == 0:
                if line.replace(' ', '').isdigit():
                    state = 1

                else:

                    if not done_first:                    
                        n_stacks = (len(line) + 1) // 4
                        for _ in range(n_stacks):
                            stacks.append('')
                        done_first = True

                    for s in range(0, n_stacks):
                        i = s * 4
                        curr = line[i:i + 4].strip()
                        if curr:
                            stacks[s] += curr[1]

            elif state == 1:
                if line.startswith('move'):
                    pieces = line.split()
                    n, fr, to = map(int, pieces[1::2])
                    moves.append([n, fr - 1, to - 1])


def do_moves():
    for (n, fr, to) in moves:
        stacks[to] = stacks[fr][:n] + stacks[to]
        stacks[fr] = stacks[fr][n:]

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    parse(f)
    do_moves()

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    tops = ''.join(s[0] for s in stacks)
    f.write(tops)
