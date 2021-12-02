### Part One

with open("day2-input.txt") as f:
    input = f.read().splitlines()

horizontal = 0
depth = 0

# finds horizontal position and depth
for i in input:
    instruction = i.split()
    direction = instruction[0]
    distance = int(instruction[1])

    if direction == "forward":
        horizontal += distance
    elif direction == "down":
        depth += distance
    elif direction == "up":
        depth -= distance

print("---Part One---")
print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Multiplied: ", depth * horizontal)


### Part Two

horizontal = 0
depth = 0
aim = 0

# finds horizontal position and depth after calculation change
for i in input:
    instruction = i.split()
    direction = instruction[0]
    amount = int(instruction[1])

    if direction == "forward":
        horizontal += amount
        depth += aim * amount
    if direction == "down":
        aim += amount
    if direction == "up":
        aim -= amount

print("\n---Part Two---")
print("Depth: ", depth)
print("Horizontal: ", horizontal)
print("Multiplied: ", depth * horizontal)


# Result:
#
# ---Part One---
# Depth:  998
# Horizontal:  1993
# Multiplied:  1989014
# 
# ---Part Two---
# Depth:  1006983
# Horizontal:  1993
# Multiplied:  2006917119