### Part One

from tabulate import tabulate

with open("day4-example.txt") as f:
    input = f.read().split("\n\n")

draw_numbers = input.pop(0).split(",")

boards = []
marked = []

for line in input:
    board = []
    rows = line.split("\n")
    for row in rows:
        row = row.split()
        row = [int(i) for i in row]
        board.append(row)

    marked.append([[False] * 5] * 5)

def check_win(board, mark):
    for row, mark_row in zip(board, mark):
        if False not in mark_row:
            return board
    for i in range(len(board[0])):
        if False not in {board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]}:
            return board
    return None

def play_number(number):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k in range(len(row)):
                if row[k] == number:
                    marked[i][j][k] = True

winning_board = None

for number in draw_numbers:
    play_number(number)
    print(number)
    
    for board, mark in zip(boards, marked):
        winning_board = (board, mark)

    if winning_board != None:
        break

print(winning_board)