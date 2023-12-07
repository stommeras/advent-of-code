import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part 1

data = input.copy()
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

all_sorted_hands = {}

# five of a kind
hands = {}

for line in list(data):
    hand, bid = line.split()
    if len(set(hand)) == 1:
        hands[hand] = bid
        data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# four of a kind
hands = {}

for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 2:
        if hand.count(unique_cards[0]) == 4 or hand.count(unique_cards[1]) == 4:
            hands[hand] = bid
            data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# full house
hands = {}

for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 2:
        if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3:
            hands[hand] = bid
            data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# three of a kind
hands = {}

for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 3:
        if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3 or hand.count(unique_cards[2]) == 3:
            hands[hand] = bid
            data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# two pair
hands = {}

for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 3:
        hands[hand] = bid
        data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# one pair
hands = {}

for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 4:
        hands[hand] = bid
        data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# high card
hands = {}

for line in list(data):
    hand, bid = line.split()
    hands[hand] = bid
    data.remove(line)

sorted_hands = dict(sorted(hands.items(), key=lambda item: [cards.index(char) for char in item[0]]))

for hand, bid in sorted_hands.items():
    all_sorted_hands[hand] = bid


# total winnings from rankings
total_winnings = 0

for index, bid in enumerate(all_sorted_hands.values()):
    total_winnings += int(bid) * (len(all_sorted_hands) - index)

print(total_winnings)


# Part 2

data = input.copy()
new_cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

five_of_a_kind = {}
four_of_a_kind = {}
full_house = {}
three_of_a_kind = {}
two_pair = {}
one_pair = {}
high_card = {}


# five of a kind
for line in list(data):
    hand, bid = line.split()
    if len(set(hand)) == 1:
        five_of_a_kind[hand] = bid
        data.remove(line)


# four of a kind
for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(set(hand)) == 2:
        if hand.count(unique_cards[0]) == 4 or hand.count(unique_cards[1]) == 4:
            if "J" in hand:
                five_of_a_kind[hand] = bid
            else:
                four_of_a_kind[hand] = bid
            data.remove(line)


# full house
for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 2:
        if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3:
            if hand.count("J") == 2 or hand.count("J") == 3:
                five_of_a_kind[hand] = bid
            elif hand.count("J") == 1:
                four_of_a_kind[hand] = bid
            else:
                full_house[hand] = bid
            data.remove(line)

# three of a kind
for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 3:
        if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3 or hand.count(unique_cards[2]) == 3:
            if hand.count("J") == 2:
                five_of_a_kind[hand] = bid
            elif hand.count("J") == 1 or hand.count("J") == 3:
                four_of_a_kind[hand] = bid
            else:
                three_of_a_kind[hand] = bid
            data.remove(line)

# two pair
for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 3:
        if hand.count("J") == 2:
            four_of_a_kind[hand] = bid
        elif hand.count("J") == 1:
            full_house[hand] = bid
        else:
            two_pair[hand] = bid
        data.remove(line)


# one pair
for line in list(data):
    hand, bid = line.split()
    unique_cards = list(set(hand))

    if len(unique_cards) == 4:
        if "J" in hand:
            three_of_a_kind[hand] = bid
        else:
            one_pair[hand] = bid
        data.remove(line)


# high card
for line in list(data):
    hand, bid = line.split()

    if "J" in hand:
        one_pair[hand] = bid
    else:
        high_card[hand] = bid
    data.remove(line)


# total ranking
card_hands = ["five_of_a_kind",
"four_of_a_kind",
"full_house",
"three_of_a_kind",
"two_pair",
"one_pair",
"high_card"]

new_all_sorted_hands = {}

for hands in card_hands:
    sorted_hands = dict(sorted(eval(hands).items(), key=lambda item: [new_cards.index(char) for char in item[0]]))

    for hand, bid in sorted_hands.items():
        new_all_sorted_hands[hand] = bid

# total winnings from rankings
new_total_winnings = 0

for index, bid in enumerate(new_all_sorted_hands.values()):
    new_total_winnings += int(bid) * (len(new_all_sorted_hands) - index)

print(new_total_winnings)