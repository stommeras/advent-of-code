### Part One

import sys
import copy

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

crates.pop(-1) # remove the line with stack numbers

stacks = [[] for x in range(len(crates[0]))]

for i in reversed(range(len(crates))):
    for y, crate in enumerate(crates[i]):
        if crate != None:
            stacks[y].append(crate)

instructionNumbers = []

for line in instructions:
    instructionLine = [int(i) for i in line.split() if i.isdigit()]
    instructionNumbers.append(instructionLine)

newStacks1 = copy.deepcopy(stacks)

for instr in instructionNumbers:
    for i in range(instr[0]):
        newStacks1[instr[2] - 1].append(newStacks1[instr[1] - 1].pop(-1))

topCrates1 = ""

for stack in newStacks1:
    topCrates1 += stack[-1]

print(topCrates1)


### Part Two

newStacks2 = copy.deepcopy(stacks)

for instr in instructionNumbers:
    moved = []
    for i in range(instr[0]):
        moved.append(newStacks2[instr[1] - 1].pop(-1))
    for j in range(len(moved)):
        newStacks2[instr[2] - 1].append(moved.pop(-1))

topCrates2 = ""

for stack in newStacks2:
    topCrates2 += stack[-1]

print(topCrates2)