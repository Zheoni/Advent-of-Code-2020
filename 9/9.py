from itertools import combinations

with open('input.txt') as file:
    seq = [int(line) for line in file]

# Part 1
preamble = 25
for i, num in enumerate(seq[preamble:], preamble):
    for (a, b) in combinations(seq[i-preamble:i], 2):
        if a + b == num:
            break
    else:
        break
print(num)

# Part 2
for l in range(2, len(seq)):
    for i in range(len(seq) - l):
        slc = seq[i:i+l]
        if sum(slc) == num:
            print(min(slc) + max(slc))
