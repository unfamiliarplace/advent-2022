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

head = Point(0, 0)
tail = Point(0, 0)

visited = {tail.sig()}

def parse_line(line: str) -> Sequence:
    s, n = line.strip().split()
    return Sequence(s, n)

def do_sequence(sequence: Sequence) -> None:
    for _ in range(sequence.n):
        head.move(sequence.diffs)
        move_tail()

def head_tail_adjacent() -> None:
    return (abs(head.x - tail.x) < 2) and (abs(head.y - tail.y) < 2)

def move_tail() -> None:
    if head_tail_adjacent():
        return
    
    else:
        x_diff, y_diff = 0, 0

        # Same column: change row
        if head.x == tail.x:
            y_diff = 1 if head.y > tail.y else -1

        # Same row: change column
        elif head.y == tail.y:
            x_diff = 1 if head.x > tail.x else -1

        # Neither: diagonal
        else:
            y_diff = 1 if head.y > tail.y else -1
            x_diff = 1 if head.x > tail.x else -1
        
        tail.move((x_diff, y_diff))
        visited.add(tail.sig())

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    for sequence in map(parse_line, f.readlines()):
        do_sequence(sequence)

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    result = len(visited)
    f.write(f'{result}')
