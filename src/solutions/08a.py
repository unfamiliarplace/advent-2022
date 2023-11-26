# https://adventofcode.com/2022/day/8

# My naming convention...
import os
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

def is_visible(n: int) -> bool:
    row = n // n_rows
    col = n % n_cols

    if row in [0, n_rows - 1] or col in [0, n_cols - 1]:
        return True

    val = grid[row][col]

    rowwise = grid[row]
    colwise = get_column(col)

    candidates = [
        max(rowwise[:col]),
        max(rowwise[col+1:]),
        max(colwise[:row]),
        max(colwise[row+1:])
    ]

    return any((c < val) for c in candidates)

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    grid = list(filter(None, map(str.strip, f.readlines())))
    n_rows = len(grid)
    n_cols = len(grid[0])
    result = sum(is_visible(n) for n in range(n_rows * n_cols))

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{result}')
