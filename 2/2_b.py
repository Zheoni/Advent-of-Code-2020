with open('input.txt') as file:
    input_list = []
    for line in file:
        parts = line.split()
        l, h = parts[0].split('-')
        policy = (int(l) - 1, int(h) - 1, parts[1][0])
        password = parts[2]
        input_list.append((policy, password))

valids = 0
for (i, j, c), password in input_list:
    l = len(password)
    if (i < l and password[i] == c) ^ (j < l and password[j] == c):
        valids += 1
print(valids)
