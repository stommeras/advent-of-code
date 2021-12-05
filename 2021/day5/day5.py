### Part One

from collections import Counter

with open("day5-input.txt") as f:
    input = f.read().splitlines()

points = []

# finding all points covered by horizontal / vertical lines
for line in input:
    segment = line.split(" -> ")
    start = segment[0].split(",")   # [x1, y1]
    end = segment[1].split(",")     # [x2, y2]
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])

    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2 + 1):
                points.append([x1, y])
        elif y1 > y2:
            for y in range(y2, y1 + 1):
                points.append([x1, y])
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2 + 1):
                points.append([x, y1])
        elif x1 > x2:
            for x in range(x2, x1 + 1):
                points.append([x, y1])

new_points = map(tuple, points)
count = Counter(new_points)

sum = 0

for k, v in count.items():
    if v >= 2:
        sum += 1

# not required for the task, but I want to print the diagram
# extremely inefficient, do not use for big input
def print_diagram(points):
    print("")

    diagram_width = 0
    diagram_heigth = 0

    for point in points:
        if point[0] + 1 > diagram_width:
            diagram_width = point[0] + 1
        if point[1] + 1 > diagram_heigth:
            diagram_heigth = point[1] + 1

    for y in range(diagram_heigth):
        for x in range(diagram_width):
            if [x, y] in points:
                print(count[x, y], end="")
            else:
                print(".",end="")
        print("")

    print("")


print("---Part One---")
# print_diagram(points)
print("Number of points where at least two lines overlap:", sum)


### Part Two

# finding diagonal lines
for line in input:
    segment = line.split(" -> ")
    start = segment[0].split(",")   # [x1, y1]
    end = segment[1].split(",")     # [x2, y2]
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])

    # x and y move in the same direction
    if x1 - x2 == y1 - y2:
        if x1 < x2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                points.append([x, y])
        elif x1 > x2:
            for x, y in zip(range(x2, x1 + 1), range(y2, y1 + 1)):
                points.append([x, y])
    # x and y move in opposite directions
    elif x1 - x2 == y2 - y1:
        if x1 < x2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
                points.append([x, y])
        elif x1 > x2:
            for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1)):
                points.append([x, y])

new_points = map(tuple, points)
count = Counter(new_points)

sum = 0

for k, v in count.items():
    if v >= 2:
        sum += 1

print("\n---Part Two---")
# print_diagram(points)
print("Number of points where at least two lines overlap:", sum)