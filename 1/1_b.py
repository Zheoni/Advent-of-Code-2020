from itertools import combinations

with open('input.txt') as file:
    input_list = [int(n) for n in file]

for (a, b, c) in combinations(input_list, 3):
    if a + b + c == 2020:
        print(a * b * c)

# for i, a in enumerate(input_list):
#     for j, b in enumerate(input_list[i+1:]):
#         for c in input_list[i+j+1:]:
#             if a + b + c == 2020:
#                 print(a * b * c)
