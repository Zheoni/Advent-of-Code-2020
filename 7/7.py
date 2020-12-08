import re

bag_re = re.compile(r'(\d+) ([\w ]+) (bags?)')

with open('input.txt') as file:
    rules = {}
    for line in file:
        items = []
        out_color, in_bags = line.split('bags contain')
        for in_bag in in_bags.split(','):
            match = bag_re.search(in_bag)
            if match:
                in_amount = int(match[1])
                in_color = match[2]
                items.append((in_amount, in_color.strip()))
        rules[out_color.strip()] = items

wanted = 'shiny gold'

r = set()
def search(bag):
    if bag in r:
        return True
    elif wanted in [contained for _, contained in rules[bag]]:
        r.add(bag)
        return True
    for _, contained in rules[bag]:
        if search(contained):
            r.add(bag)
            return True
    return False

for bag in rules:
    search(bag)
print(len(r))

def count(bag):
    n = 0
    for amount, contained in rules[bag]:
        n += amount + amount * count(contained)
    return n
print(count(wanted))
