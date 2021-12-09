### Part One

with open("day9-input.txt") as f:
    input = f.read().strip().splitlines()

numbers = [int(x) for x in input]

not_valid = None

# finds the first number that isn't a sum of two unique numbers
# in the 25 previous numbers
for i in range(25, len(numbers)):
    num = numbers[i]
    prev = [numbers[j] for j in range(i - 25, i)]
    for p in prev:
        if num - p in prev and num - p != p:
            not_valid = None
            break
        not_valid = num
    if not_valid == None:
        continue
    else:
        break
        
print("---Part One---")
print("First invalid number:", not_valid)


### Part Two

# check if you can add contiguous numbers together that add to the 
# invalid number from Part One
def check_sum(i, num):
    cont_numbers = []
    for j in range(i, len(numbers)):
        cont_numbers.append(numbers[j])
        if sum(cont_numbers) < num: 
            continue
        elif sum(cont_numbers) > num: 
            return None
        else:
            return cont_numbers

cont_numbers = []

# start the check_sum from each index in numbers
for i in range(len(numbers)):
    cont_numbers = check_sum(i, not_valid)
    if cont_numbers == None:
        continue
    else:
        break

weakness = min(cont_numbers) + max(cont_numbers)

print("\n---Part Two---")
print("Excryption weakness:", weakness)