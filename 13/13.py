from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

with open('input.txt') as file:
    earliest = int(file.readline())
    buses = [int(bus) if bus != 'x' else bus for bus in file.readline().split(',')]

t = earliest
my_bus = None
while not my_bus:
    for bus in filter(lambda b: b != 'x', buses):
        if t % bus == 0:
            my_bus = bus
            break
    else:
        t += 1

print(my_bus * (t - earliest))

t = 0
step = buses[0]
for i, bus in enumerate(buses):
    if bus == 'x':
        continue
    while (t+i) % bus != 0:
        t += step
    step = lcm(step, bus)

print(t)
