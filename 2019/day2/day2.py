#!/usr/bin/env python
import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split(",")

code = [int(x) for x in input]

i = 0

def calc(noun, verb):
    while code[i] != 99:
        if code[i] == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]

        elif code[i] == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        
        else:
            print("what happen")
            break

        i += 4

print((",".join(str(a) for a in code)))
