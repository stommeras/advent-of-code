### Part one

with open("day1-input.txt") as f:
    input = f.read().splitlines()

depths = [int(n) for n in input]

# check for each element of list if it's bigger than the previous element, and adds to num
def check_increases(list):
    sum = 0
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            sum += 1
    return sum

increases_depth = check_increases(depths)

print(increases_depth)
# 1688


### Part two

depth_windows = []

# check if 3 numbers left, adds the next three together and adds to new list
for i in range(0, len(depths)):
    if (i + 2) == (len(depths)):
        break
    else:
        depth_windows.append(depths[i] + depths[i + 1] + depths[i + 2])

increases_depth_windows = check_increases(depth_windows)

print(increases_depth_windows)