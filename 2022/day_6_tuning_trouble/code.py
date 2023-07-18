#! /usr/bin/python3

import os

def read_file():
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r')
    text = f.read()
    f.close()
    return text

def solution(text, unique):
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

def better_solution(text, unique):
    buffer = set()
    i = j = 0
    while j < len(text):
        if text[j] not in buffer:
            buffer.add(text[j])
        else:
            while i < j:
                if text[i] == text[j]:
                    i += 1
                    break
                else:
                    buffer.remove(text[i])
                i += 1
        j += 1
        if len(buffer) == unique:
            return j

if __name__ == "__main__":
    text = read_file()
    print(better_solution(text, 4))
    print(better_solution(text, 14))