with open("input.txt") as file:
    initialization = [line.strip().split(" = ") for line in file]

# Part 1
mask = 'X'*36
memory = {}
for instruction, value in initialization:
    if instruction == 'mask':
        mask = value
    elif instruction.startswith('mem'):
        value = int(value)
        addr = int(instruction[4:-1])
        for index, c in enumerate(reversed(mask)):
            if c == '1':
                value |= (1 << index)
            elif c == '0':
                value &= ~(1 << index)
        memory[addr] = value

print(sum(memory.values()))

# Part 2
mask = 'X'*36
memory = {}
for instruction, value in initialization:
    if instruction == 'mask':
        mask = value
    elif instruction.startswith('mem'):
        value = int(value)
        addrs = [int(instruction[4:-1])]
        for index, c in enumerate(reversed(mask)):
            if c == '1':
                addrs = [addr | (1 << index) for addr in addrs]
            elif c == 'X':
                new_addrs = []
                for addr in addrs:
                    addr0 = addr & ~(1 << index)
                    addr1 = addr | (1 << index)
                    new_addrs.append(addr0)
                    new_addrs.append(addr1)
                addrs = new_addrs
        for addr in addrs:
            memory[addr] = value

print(sum(memory.values()))
