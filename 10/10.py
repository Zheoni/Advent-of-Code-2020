from itertools import groupby

with open('input.txt') as file:
    adapters = sorted([int(line) for line in file])
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)

# Part 1
difs = []
for a, b in zip(adapters[:-1], adapters[1:]):
    difs.append(b - a)

print(difs.count(1) * difs.count(3))

# Part 2
difs = ''.join([str(i) for i in difs]).split('3')
print(2**difs.count('11') * 4**difs.count('111') * 7**difs.count('1111'))
