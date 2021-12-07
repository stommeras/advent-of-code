### Part One

with open("day7-input.txt") as f:
    input = f.read().split(",")

crabs = [int(x) for x in input]

def align(pos):
    total_fuel = 0

    for crab in crabs:
        total_fuel += abs(crab - pos)

    return total_fuel

least_fuel = align(0)

for i in range(max(crabs)):
    fuel = align(i)
    if fuel < least_fuel:
        least_fuel = fuel

print("---Part One---")
print(f"Least fuel possible: {least_fuel}")


### Part Two

def align_2(pos):
    total_fuel = 0

    for crab in crabs:
        steps = abs(crab - pos)
        fuel = 0
        for i in range(steps):
            fuel += i + 1
        total_fuel += fuel
            
    return total_fuel

least_fuel = align_2(0)

for i in range(max(crabs)):
    fuel = align_2(i)
    if fuel < least_fuel:
        least_fuel = fuel   

print("\n---Part Two---")
print(f"Least fuel possible: {least_fuel}")