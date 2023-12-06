import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n\n")

# Part 1


def part_1(input):
    seeds = [int(seed) for seed in input[0].split(": ")[1].split()]

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    mappings = [
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temperature",
        "temperature_to_humidity",
        "humidity_to_location",
    ]

    for section in input:
        if section.startswith("seeds:"):
            continue

        section = section.split("\n")
        mapping = section[0].split()[0].replace("-", "_")
        data = section[1:]

        for line in data:
            dest_range_start, src_range_start, length = line.split()

            eval(mapping).append(
                [int(src_range_start), int(dest_range_start), int(length)]
            )

    seed_locations = []

    for seed in seeds:
        current = seed

        for mapping in mappings:
            for line in eval(mapping):
                src, dest, length = line[0], line[1], line[2]

                if src <= current <= (src + length):
                    current = dest + current - src
                    break

        seed_locations.append(current)

    return min(seed_locations)


print(part_1(input))


# Part 2


def part_2(input):
    seeds = [int(seed) for seed in input[0].split(": ")[1].split()]
    seed_ranges = []

    i = 0
    while i < len(seeds):
        seed_ranges.append([seeds[i], seeds[i + 1]])
        i += 2

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    mappings = [
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temperature",
        "temperature_to_humidity",
        "humidity_to_location",
    ]

    for section in input:
        if section.startswith("seeds:"):
            continue

        section = section.split("\n")
        mapping = section[0].split()[0].replace("-", "_")
        data = section[1:]

        for line in data:
            dest_range_start, src_range_start, length = line.split()

            eval(mapping).append(
                [int(src_range_start), int(dest_range_start), int(length)]
            )

    seed_locations = []

    for seed_range in seed_ranges:
        # current =

        for mapping in mappings:
            for line in eval(mapping):
                src, dest, length = line[0], line[1], line[2]

                if src <= current <= (src + length):
                    current = dest + current - src
                    break

        seed_locations.append(current)

    return min(seed_locations)

print(part_2(input))