#! /usr/bin/python3

import os

def read_file():
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def part_solution(text, unique):
    i = j = 0
    buffer = set()
    while j < len(text):
        if text[j] in buffer:
            buffer.clear()
            buffer.add(text[j])
            for k in range(j - 1, j - unique, -1):
                if text[k] == text[j]:
                    i = k + 1
                    break
                else:
                    buffer.add(text[k])
        else:
            buffer.add(text[j])
        j += 1
        if len(buffer) == unique:
            break

    return j

if __name__ == "__main__":
    text = read_file()
    print(part_solution(text, 4))
    print(part_solution(text, 14))