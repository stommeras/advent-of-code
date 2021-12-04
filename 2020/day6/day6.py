### Part One

with open("day6-input.txt") as f:
    input = f.read().split("\n\n")

groups = []

for line in input:
    groups.append(line.replace("\n", ""))

counts_any = []

# using set to find unique characters
for group in groups:
    counts_any.append(len("".join(set(group))))

print("---Part One---")
print("Sum of answers anyone in a group answered yes to:", sum(counts_any))


### Part Two

groups2 = []

for line in input:
    groups2.append(line.split("\n"))

counts_every = []

# using intersection of sets to find unique characters
# present in all answers within a group
for group in groups2:
    answers = set(group[0]).intersection(*group)
    counts_every.append(len(answers))

print("\n---Part Two---")
print("Sum of answers everyone in a group answered yes to:", sum(counts_every))