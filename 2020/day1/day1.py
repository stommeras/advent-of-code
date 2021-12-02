### Part One

with open("day1-input.txt") as f:
    input = f.read().splitlines()

expenses = [int(n) for n in input]

# finds two numbers that add to 2020 and returns them
def find2020_2(list):
    for n in list:
        for m in list:
            if n + m == 2020:
                return(n, m)

n, m = find2020_2(expenses)

print("---Part One---")
print("Entry 1: ", n)
print("Entry 2: ", m)
print("Product: ", n * m)


### Part Two

# finds three numbers that add to 2020 and returns them
def find2020_3(list):
    for n in list:
        for m in list:
            for o in list:
                if n + m + o == 2020:
                    return(n, m, o)

a, b, c = find2020_3(expenses)

print("\n---Part Two---")
print("Entry 1: ", a)
print("Entry 2: ", b)
print("Entry 2: ", c)
print("Product: ", a * b * c)