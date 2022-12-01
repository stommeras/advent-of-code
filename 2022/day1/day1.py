### Part One
import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n\n")

groups = [line.splitlines() for line in input]
calories = [sum(int(i) for i in group) for group in groups]
highest = max(calories)

print(highest)


### Part Two

topThree = []

topThree.append(max(calories))
calories.remove(max(calories))
topThree.append(max(calories))
calories.remove(max(calories))
topThree.append(max(calories))

print(sum(topThree))