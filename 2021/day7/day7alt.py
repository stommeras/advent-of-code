### Part One

from numpy import *

with open("day7-input.txt") as f:
    input = f.read().split(",")

crabs = [int(x) for x in input]

# least fuel when linear fuel consumption is the median of the positions
least_fuel = sum(abs(crabs - median(crabs)))

print("---Part One--_")
print(least_fuel)


### Part Two

# the solution is guaranteed to be withing 0,5 of the mean
# so can just check mean-1 and mean+1
fuel = lambda d: d*(d+1)/2  # triangle numbers

least_fuel = min(sum(fuel(abs(crabs - floor(mean(crabs))))),
                 sum(fuel(abs(crabs - ceil(mean(crabs))))))

print("\n---Part Two---")
print(least_fuel)