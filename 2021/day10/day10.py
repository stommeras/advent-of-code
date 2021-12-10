### Part One

with open("day10-input.txt") as f:
    input = f.read().strip().splitlines()

close_to_open = {")": "(", "]": "[", "}": "{", ">": "<"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
total = 0

# find corrupted lines (wrong closer), and add score to total
for line in input:
    stack = []

    for char in list(line):
        if char in close_to_open.values():
            stack.append(char)
        elif not stack or stack.pop() != close_to_open[char]:
            total += points[char]
            break

print("---Part One---")
print("Syntax error score:", total)


### Part Two

points2 = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

# complete incomplete lines (missing closers)
for line in input:
    stack = []

    for char in list(line):
        if char in close_to_open.values():
            stack.append(char)
        elif not stack or stack.pop() != close_to_open[char]:
            stack = None
            break

    if stack:
        subtotal = 0

        for char in stack[::-1]:
            subtotal = 5 * subtotal + points2[char]

        scores.append(subtotal)

middle_score = sorted(scores)[len(scores) // 2]

print("\n---Part Two---")
print("Middle score:", middle_score)