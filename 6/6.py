with open('input.txt') as file:
    groups = [[set(person) for person in group.splitlines()]
              for group in file.read().strip().split('\n\n')]
# Part 1
print(sum([len(set.union(*group)) for group in groups]))
# Part 2
print(sum([len(set.intersection(*group)) for group in groups]))
