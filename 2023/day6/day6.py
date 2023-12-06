import sys
from math import prod

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n")

# Part 1

times = [int(time) for time in input[0].split()[1:]]
distances = [int(dist) for dist in input[1].split()[1:]]

ways_to_win = {}

for i in range(len(times)):
    ways_to_win[i] = 0

    for time in range(times[i]):
        speed = time
        distance = speed * (times[i] - time)
        if distance > distances[i]:
            ways_to_win[i] += 1

print(prod(ways_to_win.values()))


# Part 2

new_time = ""
new_distance = ""

new_ways_to_win = 0

for i in range(len(times)):
    new_time += str(times[i])
    new_distance += str(distances[i])

new_time, new_distance = int(new_time), int(new_distance)

for i in range(new_time):
    speed = i
    distance = speed * (new_time - i)
    if distance > new_distance:
        new_ways_to_win = new_time - i * 2 + 1
        break

print(new_ways_to_win)
