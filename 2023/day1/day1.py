import sys
import re

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part one

sum1 = 0

# for line in input:
#     calibrationValue = re.sub(r'[^0-9]', '', line)
#     sum1 += int(calibrationValue[0] + calibrationValue[-1])

# print(sum1)


# Part two

sum2 = 0

for line in input:
    line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    calibrationValue = re.sub(r"[^0-9]", "", line)
    sum2 += int(calibrationValue[0] + calibrationValue[-1])

print(sum2)
