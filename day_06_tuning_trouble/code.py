#! /usr/bin/python3

import os


# pylint: disable=C0116
def read_file():
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/input", "r", encoding="utf-8"
    ) as f:
        text = f.read()
    return text


# pylint: disable=C0116
def solution(text, unique):
    j = 0
    buffer = set()
    while j < len(text):
        if text[j] in buffer:
            buffer.clear()
            buffer.add(text[j])
            for k in range(j - 1, j - unique, -1):
                if text[k] == text[j]:
                    break
                buffer.add(text[k])
        else:
            buffer.add(text[j])
        j += 1
        if len(buffer) == unique:
            break

    return j


# pylint: disable=C0116
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
                buffer.remove(text[i])
                i += 1
        j += 1
        if len(buffer) == unique:
            return j
    return None


if __name__ == "__main__":
    text = read_file()
    print(better_solution(text, 4))
    print(better_solution(text, 14))
