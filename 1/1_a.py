with open('input.txt') as file:
    input_list = [int(n) for n in file]

for idx, a in enumerate(input_list):
    for b in input_list[idx + 1:]:
        if a + b == 2020:
            print(a * b)
