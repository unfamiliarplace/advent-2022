# https://adventofcode.com/2022/day/1

N = 3
IS = 'a'
OS = 'a'

total = 0

with open(f'src/inputs/{N:0>2}{IS}.txt', 'r') as f:
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

with open(f'src/outputs/{N:0>2}{OS}.txt', 'w') as f:
    f.write(f'{total}')
