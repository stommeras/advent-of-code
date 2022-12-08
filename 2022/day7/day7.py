### Part One

import sys
from collections import defaultdict
from itertools import accumulate

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()

directories = defaultdict(int)

for line in input:
    match line.split():
        case "$", "cd", "/": currentDirectory = ["/"]
        case "$", "cd", "..": currentDirectory.pop()
        case "$", "cd", x: currentDirectory.append(x + "/")
        case "$", "ls": pass
        case "dir", _: pass
        case size, _:
            for p in accumulate(currentDirectory):
                directories[p] += int(size)

sum1 = sum(s for s in directories.values() if s <= 100_000)
print(sum1)

### Part Two

delete = min(s for s in directories.values() if s >= directories["/"] - 40_000_000)

print(delete)