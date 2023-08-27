#! /usr/bin/python3

import os

with open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r') as f:
    text = f.read()

# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

# Rock = 1, Paper = 2, Scissors = 3
# Win = 6, Draw = 3, Lost = 0

rules = {
    'A': {
        'Z': 0,
        'Y': 6,
        'X': 3
    },
    'B': {
        'X': 0,
        'Z': 6,
        'Y': 3
    },
    'C': {
        'Y': 0,
        'X': 6,
        'Z': 3
    }
}
points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

rounds = text.split('\n')
#rounds = ['A Y', 'B X', 'C Z']
result = 0
for round in rounds:
    result += rules[round[0]][round[2]] + points[round[2]]

print(result)

output = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1
    }
}
points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

result = 0
for round in rounds:
    result += output[round[0]][round[2]] + points[round[2]]

print(result)