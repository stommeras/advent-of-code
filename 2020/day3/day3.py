### Part One

with open("day3-input.txt") as f:
    input = f.read().splitlines()

# check if tree encountered for every move, given x and y input
def check_trees(x_dist, y_dist):
    x = y = trees = 0
    while y < len(input):
        if input[y][x] == "#":
            trees += 1

        # loops back with % since terrain repeats
        x = (x + x_dist) % (len(input[0]))
        y += y_dist
    
    return trees

print("---Part One---")
print("Right 3, down 1")
print("Trees encountered: ", check_trees(3, 1))


### Part Two

# checking more combinations of moves
num_trees = [check_trees(1, 1),
            check_trees(3, 1),
            check_trees(5, 1),
            check_trees(7, 1),
            check_trees(1, 2)]

product = num_trees[0] * num_trees[1] * num_trees[2] * num_trees[3] * num_trees[4]

print("\n---Part Two---")
print("Right 1, down 1")
print("Trees encountered: ", num_trees[0])
print("Right 3, down 1")
print("Trees encountered: ", num_trees[1])
print("Right 5, down 1")
print("Trees encountered: ", num_trees[2])
print("Right 7, down 1")
print("Trees encountered: ", num_trees[3])
print("Right 1, down 2")
print("Trees encountered: ", num_trees[4])
print("\nMultiplied: ", product)