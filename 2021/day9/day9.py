### Part One

from collections import Counter

with open("day9-input.txt") as f:
    input = f.read().strip().splitlines()

low_points = []

list = []

for line in input:
    list.append([int(n) for n in line])

# finds low points by checking adjacent numbers (if they exist)
for i in range(len(list)):
    for j in range(len(list[i])):
        num = list[i][j]
        adj = []

        if i != 0:
            adj.append(list[i-1][j])   # above
        if i != len(list) - 1:
            adj.append(list[i+1][j])   # below
        if j != 0:
            adj.append(list[i][j-1])   # left
        if j != len(list[i]) - 1:
            adj.append(list[i][j+1])   # right

        if all(num < n for n in adj):   # checks num against all adjacent values
            low_points.append(num)

sum_risk = sum([n + 1 for n in low_points])

print("---Part One---")
print("Sum of risk levels:", sum_risk)


### Part Two

def basin(i, j):
    downhill = None
    for (di, dj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:       # adjacent values of (i, j)
        if di in range(len(list)) and dj in range(len(list[0])):
            if list[i][j] > list[di][dj]:
                downhill = (di, dj)
    
    if downhill is None:
        return (i, j)
    ret = basin(*downhill)
    return ret

basins = []

for i in range(len(list)):
    for j in range(len(list[0])):
        if list[i][j] != 9:
            basins.append(basin(i, j))

ret = 1
for basin, common in Counter(basins).most_common(3):
    ret *= common

print("\n---Part Two---")
print("Product of sizes of the three largest basins:", ret)