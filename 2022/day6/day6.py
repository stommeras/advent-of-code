### Part One

import sys

with open(sys.argv[1], "r") as f:
    input = f.read()

i = 3
posMarker = 1

while i < len(input):
    temp_set = {input[i-3], input[i-2], input[i-1], input[i]}
    if len(temp_set) == 4:
        posMarker += i
        break
    i += 1

print(posMarker)


### Part Two

j = 13
posMessage = 1

while j < len(input):
    temp_set = {input[x] for x in range(j-13, j)}
    if len(temp_set) == 13:
        posMessage += j
        break
    j += 1

print(posMessage)