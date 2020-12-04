with open("input.txt") as file:
    passports = []
    for p in [ p.replace('\n', ' ') for p in file.read().split('\n\n') ]:
        d = {}
        for field in p.strip().split(' '):
            k, v = field.split(':')
            d[k] = v
        passports.append(d)

required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

valid = 0
for passport in passports:
    for field in required:
        if field not in passport:
            break
    else:
        valid += 1

print(valid)
