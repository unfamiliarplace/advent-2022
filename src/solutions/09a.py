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

    def get_mover(s: str) -> Callable:
        if s == 'U':
            return Point.N
        elif s == 'D':
            return Point.S
        elif s == 'R':
            return Point.E
        elif s == 'L':
            return Point.W
    
    def N(self: Self) -> None:
        self.y += 1

    def S(self: Self) -> None:
        self.y -= 1

    def E(self: Self) -> None:
        self.x += 1

    def W(self: Self) -> None:
        self.x -= 1

    def N_new(self: Self) -> Self:
        return Point(self.x, self.y + 1)

    def S_new(self: Self) -> Self:
        return Point(self.x, self.y - 1)

    def E_new(self: Self) -> Self:
        return Point(self.x + 1, self.y)

    def W_new(self: Self) -> Self:
        return Point(self.x - 1, self.y)
    
    def diff(self: Self, other: Self) -> tuple[int]:
        return other.x - self.x, other.y - self.y

    def sig(self: Self) -> tuple[int]:
        return self.x, self.y
    
    def __repr__(self: Self) -> str:
        return f'{self.sig()}'
    
class Sequence:
    move: Callable
    n: int

    def __init__(self: Self, direction: str, n: str) -> None:
        self.move, self.n = Point.get_mover(direction), int(n)

sequences = []

head = Point(0, 0)
tail = Point(0, 0)

visited = {tail.sig()}

def parse_line(line: str) -> Sequence:
    s, n = line.strip().split()
    return Sequence(s, n)

def do_sequence(sequence: Sequence) -> None:
    for _ in range(sequence.n):
        sequence.move(head)
        move_tail()

def head_tail_adjacent() -> None:
    return (abs(head.x - tail.x) < 2) and (abs(head.y - tail.y) < 2)

def move_tail() -> None:
    if head_tail_adjacent():
        return
    
    else:
        if (head.y - tail.y) > 1:
            tail.N()
        elif (tail.y - head.y) > 1:
            tail.S()
        if (head.x - tail.x) > 1:
            tail.E()
        elif (tail.x - head.x) > 1:
            tail.W()

        visited.add(tail.sig())

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    for sequence in map(parse_line, f.readlines()):
        do_sequence(sequence)

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    result = len(visited)
    f.write(f'{result}')
