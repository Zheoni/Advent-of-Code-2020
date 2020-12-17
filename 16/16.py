with open('input.txt') as file:
    rules = {}
    r, mt, nt = file.read().split('\n\n')
    for rule in r.strip().splitlines():
        name, ranges_str = rule.split(':')
        ranges = []
        for _range in ranges_str.strip().split(' or '):
            low, high = _range.split('-')
            ranges.append(list(range(int(low), int(high) + 1)))
        rules[name.strip()] = ranges

    my_ticket = [int(n) for n in mt.splitlines()[1].split(',')]
    nearby_tickets = [[int(n) for n in t.split(',')] for t in nt.splitlines()[1:]]

# Part 1
invalid = []
for ticket in nearby_tickets:
    for value in ticket:
        match = False
        for ranges in rules.values():
            for r in ranges:
                if value in r:
                    match = True
        if not match:
            invalid.append(value)
print(sum(invalid))

# Part 2
for i, ticket in reversed(list(enumerate(nearby_tickets))):
    for value in ticket:
        match = False
        for ranges in rules.values():
            for r in ranges:
                if value in r:
                    match = True
        if not match:
            del nearby_tickets[i]
            break

tickets = list(nearby_tickets)
tickets.append(my_ticket)


candidate_fields = {}
for field in rules:
    candidate_fields[field] = set()
    for i in range(len(rules)):
        if all(ticket[i] in rules[field][0] or ticket[i] in rules[field][1] for ticket in tickets):
            candidate_fields[field].add(i)

indices = {}
for field, candidates in sorted(candidate_fields.items(), key=lambda x: len(x[1])):
    if len(candidates) > 1:
        candidates -= set(indices.values())
    indices[field] = candidates.pop()

p = 1
for field in indices:
    if 'departure' in field:
        p *= my_ticket[indices[field]]
print(p)
