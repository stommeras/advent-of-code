### Part One

from tabulate import tabulate

with open("day4-input.txt") as f:
    input = f.read().split("\n\n")

draw_numbers = input.pop(0).split(",")

for i in range(len(draw_numbers)):
    draw_numbers[i] = int(draw_numbers[i])

boards = []
all_drawn = []     # drawn numbers on each board

for line in input:
    board = line.replace("\n", " ")
    board = board.split()

    for i in range(len(board)):
        board[i] = int(board[i])

    boards.append(board)
    all_drawn.append([0] * 25)

def check_win(drawn):
    for i in range(0, 25, 5):
        if 0 not in {drawn[0 + i], drawn[1 + i], drawn[2 + i], drawn[3 + i], drawn[4 + i]}:
            return True
    for j in range(5):
        if 0 not in {drawn[0 + j], drawn[5 + j], drawn[10 + j], drawn[15 + j], drawn[20 + j]}:
            return True

def play_number(number):
    for board, drawn in zip(boards, all_drawn):
        for i in range(len(board)):
            if board[i] == number:
                drawn[i] = 1        

winning_board = None
winning_mark = None
winning_number = None

for number in draw_numbers:
    play_number(number)

    for i, drawn in enumerate(all_drawn):
        if check_win(drawn):
            winning_board = boards[i]
            winning_drawn = all_drawn[i]
            winning_number = number
            break

    if winning_board != None:
        break

winning_score = 0

for number, drawn in zip(winning_board, winning_drawn):
    if drawn == 0:
        winning_score += number

winning_score = winning_score * winning_number

print("---Part One---")
print("Final score of the winning board:", winning_score)


### Part Two

all_drawn = []

for board in boards:
    all_drawn.append([0] * 25)

last_board = None
last_drawn = None
last_number = None

for number in draw_numbers:
    play_number(number)

    for i, (board, drawn) in enumerate(zip(boards, all_drawn)):
        if check_win(drawn):
            if len(boards) == 1:
                last_board = board
                last_drawn = drawn
                last_number = number
                break
            else:
                boards.remove(board)
                all_drawn.remove(drawn)

    if last_board != None:
        break

last_score = 0

for number, drawn in zip(last_board, last_drawn):
    if drawn == 0:
        last_score += number

last_score = last_score * last_number

print("\n---Part Two---")
print("Final score of the losing board:", last_score)