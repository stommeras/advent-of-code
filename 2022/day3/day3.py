### Part One

import sys

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()

sum1 = 0

for line in input:
    first, second = line[:len(line)//2], line[len(line)//2:]

    common = list(set(first) & set(second))[0]
    
    if common.isupper():
        sum1 += ord(common) - 38
    else:
        sum1 += ord(common) - 96
    
print(sum1)


### Part Two

i = 0
sum2 = 0

while i < len(input):
    badge = list(set(input[i]) & set(input[i + 1]) & set(input[i + 2]))[0]
    
    if badge.isupper():
        sum2 += ord(badge) - 38
    else:
        sum2 += ord(badge) - 96

    i += 3

print(sum2)