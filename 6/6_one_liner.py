print([sum([len(op(*group)) for group in [[set(person) for person in group.splitlines()] for group in open('input.txt').read().strip().split('\n\n')]]) for op in [set.union, set.intersection]])
