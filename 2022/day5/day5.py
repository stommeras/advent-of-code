### Part One

import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n\n")

crates = input[0].splitlines()
instructions = input[1].splitlines()

for index, line in enumerate(crates):
    i = 1
    temp = []

    while i < len(line):
        if line[i] == " ":
            temp.append(None)
        else:
            temp.append(line[i])
        i += 4

    crates[index] = temp

print(crates)