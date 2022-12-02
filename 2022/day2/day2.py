### Part One

import sys

with open(sys.argv[1], "r") as f:
    input = f.read().splitlines()

# rock      - A - X - 1
# paper     - B - Y - 2
# scissors  - C - Z - 3

score1 = 0

for line in input:
    op, me = line.split()

    if op == "A":
        if me == "X":
            score1 += (3 + 1)
        elif me == "Y":
            score1 += (6 + 2)
        elif me == "Z":
            score1 += (0 + 3)
    elif op == "B":
        if me == "X":
            score1 += (0 + 1)
        elif me == "Y":
            score1 += (3 + 2)
        elif me == "Z":
            score1 += (6 + 3)
    elif op == "C":
        if me == "X":
            score1 += (6 + 1)
        elif me == "Y":
            score1 += (0 + 2)
        elif me == "Z":
            score1 += (3 + 3)

print(score1)


### Part Two

score2 = 0

# rock      - A - 1
# paper     - B - 2
# scissors  - C - 3

# lose      - X
# draw      - Y
# win       - Z

for line in input:
    op, res = line.split()

    if res == "X":
        if op == "A":
            score2 += 3
        elif op == "B":
            score2 += 1
        elif op == "C":
            score2 += 2
    
    elif res == "Y":
        score2 += 3
        if op == "A":
            score2 += 1
        elif op == "B":
            score2 += 2
        elif op == "C":
            score2 += 3

    elif res == "Z":
        score2 += 6
        if op == "A":
            score2 += 2
        elif op == "B":
            score2 += 3
        elif op == "C":
            score2 += 1

print(score2)
