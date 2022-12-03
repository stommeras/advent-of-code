#!/usr/bin/env python
 
import math
import sys

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()

# part one

req1 = []

for i in input:
    req1.append((math.floor(int(i) / 3)) - 2)

print(sum(req1))


# part two

req2 = []

for i in input:
    total = 0

    while True:
        i = (math.floor(int(i) / 3)) - 2
        if i <= 0:
            break
        total += i
    
    req2.append(total)

print(sum(req2))