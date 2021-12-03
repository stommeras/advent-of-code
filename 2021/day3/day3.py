### Part One

from tabulate import tabulate
import copy

with open("day3-input.txt") as f:
    input = f.read().splitlines()

# finding the most common bit for each position
def find_most_common_bits(list):
    zeroes = [0] * len(list[0])
    ones = [0] * len(list[0])
    for i in range(0, len(input[0])):
        for line in list:
            if line[i] == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1
    return zeroes, ones

zeroes, ones = find_most_common_bits(input)

gamma = ""
epsilon = ""

# concatenating gamma and epsilon as strings
for a, b in zip(zeroes, ones):
    if a > b:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

print("---Part One---")
print(tabulate([["Gamma rate: ", gamma, "decimal: ", int(gamma, 2)],
                ["Epsilon rate: ", epsilon, "decimal: ", int(epsilon, 2)]]))
print("Power consumption: ", int(gamma, 2) * int(epsilon, 2))


### Part Two

# Finding ratings, a and b determines if looking for
# most common or least common
def find_rating(data, a, b):
    for i in range(0, len(input[0])):
        number_to_remove = ""
        to_remove = []

        zeroes, ones = find_most_common_bits(data)

        if ones[i] > zeroes[i]:
            number_to_remove = a
        elif ones[i] == zeroes[i]:
            number_to_remove = a
        else:
            number_to_remove = b
        
        for line in data:
            if line[i] == number_to_remove:
                to_remove.append(line)

        for line in to_remove:
            data.remove(line)

        if len(data) == 1:
            break
    return data[0]

oxygen_data = copy.copy(input)
co2_data = copy.copy(input)

oxygen_generator_rating = find_rating(oxygen_data, "0", "1")
co2_scrubber_rating = find_rating(co2_data, "1", "0")

print("\n---Part Two---")
print(tabulate([["Oxygen generator rating: ", oxygen_generator_rating, "decimal: ", int(oxygen_generator_rating, 2)],
                ["CO2 scrubber rating: ", co2_scrubber_rating, "decimal: ", int(co2_scrubber_rating, 2)]]))
print("Life support rating: ", int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))