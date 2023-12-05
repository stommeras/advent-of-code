import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part 1

sum1 = 0

for line in input:
    cards = line.split(": ")[1]

    winning, mine = cards.split(" | ")
    winning = set(winning.split())
    mine = set(mine.split())

    num_matches = len(winning.intersection(mine))
    if num_matches > 0:
        sum1 += 2 ** (num_matches - 1)

print(sum1)


# Part 2

number_of_cards = {}

for i in range(len(input)):
    number_of_cards[i+1] = 1

for line in input:
    game, cards = line.split(": ")
    game = int(game.split()[1])

    winning, mine = cards.split(" | ")
    winning = set(winning.split())
    mine = set(mine.split())

    num_matches = len(winning.intersection(mine))

    for x in range(number_of_cards[game]):
        for i in range(num_matches):
            number_of_cards[game + i + 1] += 1

print(sum(number_of_cards.values()))