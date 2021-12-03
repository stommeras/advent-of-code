### Part One

with open("day5-input.txt") as f:
    input = f.read().splitlines()

seat_ids = []

# the code on boarding pass is literally just binary
for line in input:    
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")

    row = int(line[:7], 2)
    column = int(line[7:], 2)
    seat_id = (row * 8) + column

    seat_ids.append(seat_id)

seat_ids.sort()

highest_seat_id = seat_ids[-1]

print("---Part One---")
print("Highest seat ID: ", highest_seat_id)


### Part Two

my_seat_id = 0

# find the missing seat id
for id in range(seat_ids[0], seat_ids[-1] + 1):
    if id not in seat_ids and id + 1 in seat_ids and id - 1 in seat_ids:
        my_seat_id = id

print("\n---Part Two---")
print("My seat ID: ", my_seat_id)