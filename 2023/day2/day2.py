### Part One
import sys
import re

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part 1

max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_of_ids = 0

for line in input:
    game_id, game = line.split(": ")
    id = int(game_id.split(" ")[1])
    sets = game.split("; ")

    valid = True

    for set in sets:
        pulls = set.split(", ")

        for pull in pulls:
            number, color = pull.split(" ")
            if int(number) > max[color]:
                valid = False

    if valid:
        sum_of_ids += id

print(sum_of_ids)


# Part 2

sum_of_powers = 0

for line in input:
    game_id, game = line.split(": ")
    identifier = int(game_id.split(" ")[1])
    sets = game.split("; ")

    highest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for set in sets:
        pulls = set.split(", ")

        for pull in pulls:
            number, color = pull.split(" ")
            if int(number) > highest[color]:
                highest[color] = int(number)

    sum_of_powers += highest["red"] * highest["green"] * highest["blue"]

print(sum_of_powers)
