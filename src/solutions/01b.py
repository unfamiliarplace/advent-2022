# https://adventofcode.com/2022/day/1

N = 1
IS = 'a'
OS = 'b'

best = []

with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
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

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{sum(best)}')
