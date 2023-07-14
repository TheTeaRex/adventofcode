#! /usr/bin/python3

with open('day_1_input', 'r') as f:
    text = f.read()

calories = text.split('\n')
elvies = []
count = 0
for calory in calories:
    if len(calory) != 0:
        count += int(calory)
    else:
        elvies.append(count)
        count = 0

elvies.sort(reverse = True)
print(sum(elvies[:3]))