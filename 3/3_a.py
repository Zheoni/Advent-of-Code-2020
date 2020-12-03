with open('input.txt') as file:
    map = [line.strip() for line in file]

h = 3
v = 1

map_height = len(map)
map_width = len(map[0])

i, j = 0, 0

trees = 0

while i < map_height:
    if map[i][j % map_width] == '#':
        trees += 1
    i += v
    j += h

print(trees)
