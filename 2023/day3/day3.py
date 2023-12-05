import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part 1

def find_whole_number(row, column):
    left_boundary = column
    while left_boundary > 0 and input_copy[row][left_boundary - 1].isdigit():
        left_boundary -= 1

    right_boundary = column
    while right_boundary < len(input_copy[row]) - 1 and input_copy[row][right_boundary + 1].isdigit():
        right_boundary += 1

    whole_number = input_copy[row][left_boundary:right_boundary + 1]
    input_copy[row] = input_copy[row][:left_boundary] + "." * len(whole_number) + input_copy[row][right_boundary + 1:]
    return whole_number

sum1 = 0

input_copy = input.copy()

for row, line in enumerate(input_copy):
    for column, char in enumerate(line):
        if not(char.isdigit() or char == "."):
            adjacent_positions = [
                (row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
                (row, column - 1),                        (row, column + 1),
                (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)
            ]

            for r, c in adjacent_positions:
                if r < 0 or c < 0 or r >= len(input_copy) or c >= len(input_copy[0]):
                    continue
                if input_copy[r][c].isdigit():
                    sum1 += int(find_whole_number(r, c))

print(sum1)


# Part 2

sum2 = 0

input_copy = input.copy()

for row, line in enumerate(input_copy):
    for column, char in enumerate(line):
        if char == "*":
            input_copy = input.copy()

            adjacent_positions = [
                (row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
                (row, column - 1),                        (row, column + 1),
                (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)
            ]

            part_numbers = []

            for r, c in adjacent_positions:
                if r < 0 or c < 0 or r >= len(input) or c >= len(input[0]):
                    continue

                if input_copy[r][c].isdigit():
                    part_numbers.append(int(find_whole_number(r, c)))

            if len(part_numbers) == 2:
                sum2 += part_numbers[0] * part_numbers[1]

print(sum2)