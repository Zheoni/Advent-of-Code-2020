with open('input.txt') as file:
    input_list = []
    for line in file:
        parts = line.split()
        l, h = parts[0].split('-')
        policy = (int(l), int(h), parts[1][0])
        password = parts[2]
        input_list.append((policy, password))

valids = 0
for policy, password in input_list:
    count = password.count(policy[2])
    if count >= policy[0] and count <= policy[1]:
        valids += 1
print(valids)
