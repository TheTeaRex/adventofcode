#! /usr/bin/python3

import collections
import copy

with open('day_5_input', 'r') as f:
    text = f.read()

lines = text.split('\n')

# part 1
# getting the number of stacks
size = 0
for _ in range(1, len(lines[0]), 4):
    size += 1

i = 0
stacks = [collections.deque() for _ in range(size)]
while i < len(lines):
    if lines[i][1].isnumeric():
        break
    for j in range(1, len(lines[i]), 4):
        if lines[i][j] != ' ':
            stacks[j // 4].appendleft(lines[i][j])
    i += 1

# deep copy for part 2's operation
stacks2 = copy.deepcopy(stacks)

# get to the rearrange log
i += 2
logstart = i
while i < len(lines):
    items = lines[i].split(' ')
    for _ in range(int(items[1])):
        crate = stacks[int(items[3]) - 1].pop()
        stacks[int(items[5]) - 1].append(crate)
    i += 1

print(''.join([stack[-1] for stack in stacks]))

# part 2
stacks = [[] for _ in range(size)]
i = 0
while i < len(lines):
    if lines[i][1].isnumeric():
        break
    i += 1
j = i - 1
while j >= 0:
    for k in range(1, len(lines[j]), 4):
        if lines[j][k] != ' ':
            stacks[k // 4].append(lines[j][k])
    j -= 1

# get to the rearrange log
i += 2
while i < len(lines):
    items = lines[i].split(' ')
    num_move = int(items[1])
    f = int(items[3]) - 1
    t = int(items[5]) - 1
    stacks[t] += stacks[f][-num_move:]
    stacks[f] = stacks[f][:len(stacks[f]) - num_move]
    i += 1

print(''.join([stack[-1] for stack in stacks]))