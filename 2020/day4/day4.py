### Part One

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) ((Optional))

import re

with open("day4-input.txt") as f:
    input = f.read().split("\n\n")

passports = []

for line in input:
    passports.append(line.replace("\n", " "))

present = []

# finds all passports with all the fields required
for passport in passports:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    
    fields = passport.split(" ")

    for field in fields:
        data = field.split(":")
        key = data[0]
        value = data[1]

        if key == "byr":
            byr = value
        elif key == "iyr":
            iyr = value
        elif key == "eyr":
            eyr = value
        elif key == "hgt":
            hgt = value
        elif key == "hcl":
            hcl = value
        elif key == "ecl":
            ecl = value
        elif key == "pid":
            pid = value

    if None in {byr, iyr, eyr, hgt, hcl, ecl, pid}:
        present.append(False)
    else:
        present.append(True)

num_present = 0

for p in present:
    if p == True:
        num_present += 1

print("---Part One---")
print("Number of present passports with correct fields: ", num_present)


### Part Two

valid = []

# finds all passports with all the fields required, and valid information
for passport in passports:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    
    fields = passport.split(" ")

    for field in fields:
        data = field.split(":")
        key = data[0]
        value = data[1]

        # checks all the given criteria for each field
        if key == "byr" and len(value) == 4 and 1920 <= int(value) <= 2002:
            byr = value
        elif key == "iyr" and len(value) == 4 and 2010 <= int(value) <= 2020:
            iyr = value
        elif key == "eyr" and len(value) == 4 and 2020 <= int(value) <= 2030:
            eyr = value
        elif key == "hgt":
            if value[-2:] == "cm" and 150 <= int(value[:len(value) - 2]) <= 193:
                hgt = value
            elif value[-2:] == "in" and 59 <= int(value[:len(value) - 2]) <= 76:
                hgt = value
        elif key == "hcl" and value[0] == "#" and len(value[1:]) == 6 and re.match('^[0123456789abcdef]+$', value[1:]):
            hcl = value
        elif key == "ecl" and value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            ecl = value
        elif key == "pid" and len(value) == 9 and re.match('^[0123456789]+$', value):
            pid = value

    if None in {byr, iyr, eyr, hgt, hcl, ecl, pid}:
        valid.append(False)
    else:
        valid.append(True)

num_valid = 0

for v in valid:
    if v == True:
        num_valid += 1

print("\n---Part Two---")
print("Number of valid passports with correct fields: ", num_valid)