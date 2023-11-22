# https://adventofcode.com/2022/day/7

from __future__ import annotations
from typing import Iterator, Self

# My naming convention...
import os
fname = os.path.basename(__file__).strip('.py')
N = int(fname[:2])
S = fname[2]

# Logic

class Node():
    def __init__(self, parent: Dir, name: str) -> None:
        self.parent, self.name = parent, name

    def get_size(self) -> int:
        raise NotImplementedError
    
    def get_all_nodes(self) -> list[Node]:
        raise NotImplementedError

class Dir(Node):
    def __init__(self, parent: Dir, name: str) -> None:
        super().__init__(parent, name)
        self.children = []
    
    def get_size(self) -> int:    
        return sum(map(lambda node: node.get_size(), self.children))
    
    def get_all_nodes(self) -> list[Node]:
        nodes = [self]
        for child in self.children:
            nodes.extend(child.get_all_nodes())
        return nodes

    def get_child_node(self, name: str) -> Node:
        for child in self.children:
            if child.name == name:
                return child

class Root(Dir):
    def __init__(self, name: str) -> None:
        super().__init__(None, name)
    
class File(Node):
    def __init__(self, parent: Dir, name: str, size: int) -> None:
        super().__init__(parent, name)
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
    def get_all_nodes(self) -> list[Node]:
        return [self]

class Tree:
    def __init__(self) -> None:
        self.root = Root('/')

    def get_free_space(self) -> int:
        return 70_000_000 - self.root.get_size()
    
    def get_deletion_need(self) -> int:
        return max(0, 30_000_000 - self.get_free_space())
    
    def get_smallest_deletable(self) -> Dir:
        deletion_need = self.get_deletion_need()
        sizes = [node.get_size() for node in self.root.get_all_nodes() if isinstance(node, Dir)]
        sizes.sort()

        for size in sizes:
            if size >= deletion_need:
                return size
    
tree = Tree()

def parse(f):
    cwd = tree.root

    # skip cd /
    f.readline()

    for line in f.readlines():
        line = line.strip()

        parts = line.split()
        
        # cd
        if parts[0] == '$' and parts[1] == 'cd':
            if (parts[2] == '..') and cwd.parent:
                cwd = cwd.parent

            else:
                cwd = cwd.get_child_node(parts[2])

        # file
        elif parts[0].isdigit():
            cwd.children.append(File(cwd, parts[1], int(parts[0])))

        # dir
        elif parts[0] == 'dir':
            cwd.children.append(Dir(cwd, parts[1]))

def get_undersize() -> list[Dir]:
    nodes = []

    for node in tree.root.get_all_nodes():

        if isinstance(node, Dir) and node.get_size() <= 100_000:
            nodes.append(node)
    
    return nodes

def sum_undersize() -> int:
    return sum(d.get_size() for d in get_undersize())

with open(f'src/inputs/{N:0>2}.txt', 'r') as f:
    parse(f)

with open(f'src/outputs/{N:0>2}{S}.txt', 'w') as f:
    f.write(f'{tree.get_smallest_deletable()}')
