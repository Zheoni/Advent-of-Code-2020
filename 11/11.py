with open('input.txt') as file:
    layout = [[c for c in line.strip()] for line in file]
current = [list(row) for row in layout]
new = [list(row) for row in layout]

def adjacent_seats(i, j, layout):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ei = i + di
            ej = j + dj
            if not(di == dj == 0) and 0 <= ei < len(layout) and 0 <= ej < len(layout[0]) :
                if layout[ei][ej] == '#':
                    count += 1
    return count

def first_see_seats(i, j, layout):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == dj == 0:
                continue
            r = 1
            while True:
                ei = i + r * di
                ej = j + r * dj
                if 0 <= ei < len(layout) and 0 <= ej < len(layout[0]):
                    seat = layout[ei][ej]
                else:
                    break
                if seat == '#':
                    count += 1
                    break
                elif seat == 'L':
                    break
                r += 1
    return count
def exec_round(current, new, tolerance, neighbor_function):
    change = False
    for i, row in enumerate(current):
        for j, seat in enumerate(row):
            n = neighbor_function(i, j, current)
            if seat == 'L' and n == 0:
                new[i][j] = '#'
                change = True
            elif seat == '#' and n >= tolerance:
                new[i][j] = 'L'
                change = True
            else:
                new[i][j] = current[i][j]
    return change

# Part 1
while exec_round(current, new, tolerance=4, neighbor_function=adjacent_seats):
    current, new = new, current

print(sum(seats.count('#') for seats in current))

# Part 2
current = layout
while exec_round(current, new, tolerance=5, neighbor_function=first_see_seats):
    current, new = new, current

print(sum(seats.count('#') for seats in current))
