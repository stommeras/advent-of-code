### Part One

with open("day2-input.txt") as f:
    input = f.read().splitlines()

valid = 0

# finding valid passwords in the database given the criteria
for n in input:
    data = n.split(" ")
    range = data[0].split("-")
    letter = data[1][0]
    password = data[2]
    
    # check if the number of the given letter is in the given range
    if int(range[0]) <= password.count(letter) <= int(range[1]):
        valid += 1

print("---Part One---")
print("Valid passwords: ", valid)


### Part Two

valid = 0

# finding valid passwords given new criteria
for n in input:
    data = n.split(" ")
    positions = data[0].split("-")
    letter = data[1][0]
    password = data[2]

    # letter can only be in exacyly one of the two positions,
    # so I check if letter is in both first
    if password[int(positions[0]) - 1] == letter and password[int(positions[1]) - 1] == letter:
        continue
    elif password[int(positions[0]) - 1] == letter or password[int(positions[1]) - 1] == letter:
        valid += 1

print("---Part Two---")
print("Valid passwords: ", valid)