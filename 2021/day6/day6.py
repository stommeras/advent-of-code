### Part One

import time

with open("day6-input.txt") as f:
    input = f.readlines()
    input = list(map(int, input[0].strip().split(",")))

fish = [input.count(i) for i in range(9)]

def fish_after_n_days(list, n):
    for i in range(n):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
        assert len(fish) == 9
    return sum(list)

days_1 = 80
sum_80 = fish_after_n_days(fish, days_1)

print("---Part One---")
print("Number of lanternfish after", days_1, "days:", sum_80)


### Part Two

fish = [input.count(i) for i in range(9)]

days_2 = 256
sum_256 = fish_after_n_days(fish, days_2)

print("\n---Part Two---")
print("Number of lanternfish after", days_2, "days:", sum_256)
