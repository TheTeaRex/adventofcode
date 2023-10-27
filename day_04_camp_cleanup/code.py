#! /usr/bin/python3

import os

with open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r') as f:
    text = f.read()

pairs = text.split('\n')

# part 1
count = 0
for pair in pairs:
    sections = pair.split(',')
    first = [int(section) for section in sections[0].split('-')]
    second = [int(section) for section in sections[1].split('-')]
    if (first[0] <= second[0] and first[1] >= second[1]) or\
        (second[0] <= first[0] and second[1] >= first[1]):
        count += 1

print(count)

# part 2
count = 0
for pair in pairs:
    sections = pair.split(',')
    first = [int(section) for section in sections[0].split('-')]
    second = [int(section) for section in sections[1].split('-')]
    if (first[0] <= second[0] <= first[1]) or\
        (second[0] <= first[0] <= second[1]) or\
        (first[0] <= second[1] <= first[1]) or\
        (second[0] <= first[1] <= second[1]):
        count += 1

print(count)