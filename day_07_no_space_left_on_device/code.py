#! /usr/bin/python3

import collections
import os

class Node:
    def __init__(self, name, is_dir, parent=None, size=0):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.size = size
        self.children = {}

    def __repr__(self):
        return self.name

    # pylint: disable=C0116
    def get_size(self):
        if self.size != 0:
            return self.size
        if not self.is_dir:
            return self.size
        total = 0
        # pylint: disable=C0206
        for item in self.children:
            total += self.children[item].get_size()
        self.size = total
        return total

    def print_tree(self, level=0):
        if self.is_dir:
            self.get_size()
            print(f'{"  " * level}- {self.name} (dir, size={self.size})')
            # pylint: disable=C0206
            for item in self.children:
                self.children[item].print_tree(level + 1)
        else:
            print(f'{"  " * level}- {self.name} (file, size={self.size})')

# pylint: disable=C0116
def read_file():
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r', encoding="utf-8") as f:
        text = f.read()
    return text

# pylint: disable=C0116
def map_filesystem_from_string(text):
    lines = text.split("\n")
    root = Node("/", True)
    current = root
    i = 0
    while i < len(lines):
        items = lines[i].split(" ")
        if items[0] == "$":
            if items[1] == "cd":
                if items[2] == "/":
                    current = root
                elif items[2] == "..":
                    current = current.parent
                else:
                    current = current.children[items[2]]
        elif items[0] == "dir":
            current.children[items[1]] = Node(items[1], True, current)
        else:  # items[0] == numeric which is a file
            current.children[items[1]] = Node(items[1], False, current, int(items[0]))
        i += 1

    return root


def solution_part_1(node, threshold):
    total = 0
    q = collections.deque([node])
    while q:
        a = q.pop()
        if a.is_dir:
            q.extend(a.children.values())
            if a.size <= threshold:
                total += a.size
    return total


def solution_part_2(node, space_needed):
    result = float("inf")
    q = collections.deque([node])
    while q:
        a = q.pop()
        if a.is_dir:
            if a.size >= space_needed:
                result = min(a.size, result)
            q.extend(a.children.values())
    return result


if __name__ == "__main__":
    text = read_file()
    root = map_filesystem_from_string(text)
    root.get_size()
    # root.print_tree()
    disk_space_available = 70000000
    minimum_disk_space_needed = 30000000
    print(solution_part_1(root, 100000))
    print(solution_part_2(root, minimum_disk_space_needed - (70000000 - root.size)))
