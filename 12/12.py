with open('input.txt') as file:
    instructions = [(line[0], int(line[1:])) for line in file.readlines()]

x = 0
y = 0
facing = 0

def move_ship(i, v):
    global x, y, facing
    if i == 'N':
        y += v
    elif i == 'S':
        y -= v
    elif i == 'E':
        x += v
    elif i == 'W':
        x -= v
    elif i == 'L':
        facing = (facing + v // 90) % 4
    elif i == 'R':
        facing = (facing - v // 90) % 4
    elif i == 'F':
        move_ship(['E', 'N', 'W', 'S'][facing], v)

for i, v in instructions:
    move_ship(i, v)
print(abs(x) + abs(y))

x = 10
y = 1
x_ship = 0
y_ship = 0

def move_waypoint(i, v):
    global x, y, x_ship, y_ship
    if i == 'N':
        y += v
    elif i == 'S':
        y -= v
    elif i == 'E':
        x += v
    elif i == 'W':
        x -= v
    elif i == 'L':
        if v == 90:
            x, y = -y, x
        elif v == 180:
            x, y = -x, -y
        elif v == 270:
            x, y = y, -x
    elif i == 'R':
        move_waypoint('L', 360 - v)
    elif i == 'F':
        x_ship += v * x
        y_ship += v * y

for i, v in instructions:
    move_waypoint(i, v)
print(abs(x_ship) + abs(y_ship))
