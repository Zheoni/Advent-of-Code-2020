with open('input.txt') as file:
    map = [line.strip() for line in file]

map_height = len(map)
map_width = len(map[0])

def traverse_map(h, v):
    i, j = 0, 0

    trees = 0

    while i < map_height:
        if map[i][j % map_width] == '#':
            trees += 1
        i += v
        j += h
    return trees

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

r = 1;
for h, v in slopes:
    trees = traverse_map(h, v)
    r *= trees

print(r)
