with open('input.txt') as file:
    seats = [[1 if c in ['B', 'R'] else 0 for c in line] for line in file]


def get_seat_id(seat_code):
    def binary_segmentation(code, l, h):
        if len(code) == 0:
            return l
        else:
            p = l + (h - l) // 2
            if code[0] == 0:
                return binary_segmentation(code[1:], l, p)
            else:
                return binary_segmentation(code[1:], p, h)

    row = binary_segmentation(seat_code[0:7], 0, 128)
    col = binary_segmentation(seat_code[7:], 0, 8)
    return row * 8 + col


# Part 1
seat_ids = [get_seat_id(seat) for seat in seats]
print(max(seat_ids))

# Part 2
for seat in seat_ids:
    if seat + 1 not in seat_ids and seat + 2 in seat_ids:
        print(seat + 1)
        break
