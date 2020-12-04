import re

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

        value = passport[field]
        try:
            if field == "byr":
                num = int(value)
                if len(value) != 4 or num < 1920 or num > 2002:
                    break
            elif field == "iyr":
                num = int(value)
                if len(value) != 4 or num < 2010 or num > 2020:
                    break
            elif field == "eyr":
                num = int(value)
                if len(value) != 4 or num < 2020 or num > 2030:
                    break
            elif field == "hgt":
                num = int(value[:-2])
                if value.endswith("cm"):
                    if num < 150 or num > 193:
                        break
                elif value.endswith("in"):
                    if num < 59 or num > 76:
                        break
                else:
                    break
            elif field == "hcl":
                if not re.compile(r'^#[0-9a-f]{6}$').match(value):
                    break
            elif field == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    break
            elif field == "pid":
                if len(value) != 9 or not value.isdigit():
                    break
        except:
            break
    else:
        valid += 1

print(valid)
