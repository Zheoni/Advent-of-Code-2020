with open('input.txt') as file:
    start = list(map(lambda n: int(n), file.read().split(',')))

def get_nth(start, nth):
    mem = {n : i+1 for i, n in enumerate(start)}
    turn = len(mem)
    last_n = list(mem.keys())[-1]
    del mem[last_n] # to keep the order
    
    while turn < nth:
        turn += 1
        last_time = mem.get(last_n, None)
        if last_time:
            del mem[last_n] # to keep the order
            next_n = turn - 1 - last_time
        else:
            next_n = 0
        mem[last_n] = turn - 1
        last_n = next_n
    return last_n
        
print(get_nth(start, 2020))
print(get_nth(start, 30000000))
