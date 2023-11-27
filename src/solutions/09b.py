# https://adventofcode.com/2022/day/9

# My naming convention...

from typing import Self, Callable
import os

fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

class Point:
    x: int
    y: int

    def __init__(self: Self, x: int, y: int) -> None:
        self.x, self. y = x, y

    def get_difference(direction: str) -> tuple[int, int]:
        if direction == 'U':
            return 0, 1
        elif direction == 'D':
            return 0, -1
        elif direction == 'R':
            return 1, 0
        elif direction == 'L':
            return -1, 0
        
    def move(self: Self, diffs: tuple[int]) -> None:
        x_diff, y_diff = diffs
        self.x += x_diff
        self.y += y_diff

    def sig(self: Self) -> tuple[int]:
        return self.x, self.y
    
    def __repr__(self: Self) -> str:
        return f'{self.sig()}'
    
class Sequence:
    diffs: tuple[int]
    n: int

    def __init__(self: Self, direction: str, n: str) -> None:
        self.diffs, self.n = Point.get_difference(direction), int(n)

sequences = []
segments = []
for _ in range(10):
    segments.append(Point(0, 0))

visited = {segments[-1].sig()}

def parse_line(line: str) -> Sequence:
    s, n = line.strip().split()
    return Sequence(s, n)

def do_sequence(sequence: Sequence) -> None:
    for _ in range(sequence.n):
        segments[0].move(sequence.diffs)
        for i in range(1, 10):            
            move_segment(i)
        visited.add(segments[-1].sig())

def adjacent(prev: Point, curr: Point) -> None:
    return (abs(prev.x - curr.x) < 2) and (abs(prev.y - curr.y) < 2)

def move_segment(i: int) -> None:
    prev = segments[i - 1]
    curr = segments[i]

    if adjacent(prev, curr):
        return
    
    else:
        x_diff, y_diff = 0, 0

        # Same column: change row
        if prev.x == curr.x:
            y_diff = 1 if prev.y > curr.y else -1

        # Same row: change column
        elif prev.y == curr.y:
            x_diff = 1 if prev.x > curr.x else -1

        # Neither: diagonal
        else:
            y_diff = 1 if prev.y > curr.y else -1
            x_diff = 1 if prev.x > curr.x else -1
        
        curr.move((x_diff, y_diff))

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    for sequence in map(parse_line, f.readlines()):
        do_sequence(sequence)

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    result = len(visited)
    f.write(f'{result}')
