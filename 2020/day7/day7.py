### Part One

with open("day7-input.txt") as f:
    input = f.read().splitlines()

# two lists with the bag colors and the colors they contain
bag_color = []
bag_contains = []

for line in input:
    line = line.replace(".", "")
    line = line.replace(" bags", "")
    line = line.replace(" bag", "")
    line = line.split(" contain ")

    color = line[0]
    contains = {}       # {bag color : number}

    contain = line[1].split(", ")

    for c in contain:
        if c == "no other":
            contains["no colors"] = None
            break

        contains[c[2:]] = int(c[0])

    bag_color.append(color)
    bag_contains.append(contains)

my_bag = "shiny gold"

# recursively finds the bags that can hold my_color
def find_outermost(bag, list):
    for color, contains in zip(bag_color, bag_contains):
        if bag in contains.keys() and color not in list:
            list.append(color)
            find_outermost(color, list)

outer_bags = []
find_outermost(my_bag, outer_bags)

print("---Part One---")
print("Number of bag colors that eventually can hold at least one shiny gold bag:", len(outer_bags))


### Part Two

# recursively add together the bags with my_bag
def find_inner_bags(bag, sum):
    sum = 0

    index = bag_color.index(bag)

    for k, v in bag_contains[index].items():
        if k == "no colors":
            return 0
        sum = sum + v + v * find_inner_bags(k, sum)
    return sum

inner_bags_sum = 0
inner_bags_sum = find_inner_bags(my_bag, inner_bags_sum)

print("\n---Part Two---")
print("Number of bags a", my_bag, "bag must contain:", inner_bags_sum)