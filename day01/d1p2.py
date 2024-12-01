"""
Advent of code 2024
Day 1 - puzzle 2

Thomas Guimezanes.
"""

left_locations = []
rigth_locations = []


def parse_locations_input(locations: str) -> tuple[int, int]:
    return (int(locations.split(" ")[0]), int(locations.split(" ")[-1]))


def count_occurences(left_locations, right_locations) -> dict[int, int]:
    return {key: right_locations.count(key) for key in left_locations}


def similarity_score(occurences: dict[int, int]) -> int:
    return sum([key*value for key, value in occurences.items()])


with open('./inputs/d1p1.txt', 'r') as inputFile:
    locations = inputFile.readlines()

for location in locations:
    left, right = parse_locations_input(location)
    left_locations.append(left)
    rigth_locations.append(right)

occurences = count_occurences(left_locations, rigth_locations)

result = similarity_score(occurences)

print(result)
