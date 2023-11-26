# https://adventofcode.com/2022/day/8

# My naming convention...
import os
import math

fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

result = 0
n_rows = 0
n_cols = 0
grid = []

def get_column(col: int) -> bool:
    return ''.join(grid[row][col] for row in range(n_rows))

def get_score(n: int) -> bool:
    row = n // n_rows
    col = n % n_cols

    val = grid[row][col]

    rowwise = grid[row]
    colwise = get_column(col)

    N = colwise[:row][::-1]
    S = colwise[row+1:]
    E = rowwise[col+1:]
    W = rowwise[:col][::-1]

    results = []
    for dir in [N, S, E, W]:
        for i in range(len(dir)):

            if dir[i] >= val:
                results.append(i + 1)
                break

        # if did not break
        else:
            results.append(len(dir))

    return math.prod(results)

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    grid = list(filter(None, map(str.strip, f.readlines())))
    n_rows = len(grid)
    n_cols = len(grid[0])

    result = max(get_score(n) for n in range(n_rows * n_cols))

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{result}')
