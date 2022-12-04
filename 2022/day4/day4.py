### Part One

import sys

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()

fully_contains = 0

for line in input:
    a_range, b_range = line.split(",")
    a_start, a_end = a_range.split("-")
    b_start, b_end = b_range.split("-")
    a = list(range(int(a_start), int(a_end) + 1))
    b = list(range(int(b_start), int(b_end) + 1))
    if all(x in a for x in b) or all(y in b for y in a):
        fully_contains += 1

print(fully_contains)

partly_contains = 0

for line in input:
    a_range, b_range = line.split(",")
    a_start, a_end = a_range.split("-")
    b_start, b_end = b_range.split("-")
    a = list(range(int(a_start), int(a_end) + 1))
    b = list(range(int(b_start), int(b_end) + 1))
    if any(x in a for x in b) or any(y in b for y in a):
        partly_contains += 1

print(partly_contains)