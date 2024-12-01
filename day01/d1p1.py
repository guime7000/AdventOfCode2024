"""
Advent of code 2024
Day 1 - puzzle 1

Thomas Guimezanes.
"""

left_locations = []
rigth_locations = []


def parse_locations_input(locations: str) -> tuple[int, int]:
    return (int(locations.split(" ")[0]), int(locations.split(" ")[-1]))


def compute_distance(left_locations: list, right_locations: list) -> list:
    return [abs(left-right) for left, right in zip(left_locations, right_locations)]


with open('../inputs/d1p1.txt', 'r') as inputFile:
    locations = inputFile.readlines()

for location in locations:
    left, right = parse_locations_input(location)
    left_locations.append(left)
    rigth_locations.append(right)

sorted_left = sorted(left_locations)
sorted_right = sorted(rigth_locations)

distance = compute_distance(sorted_left, sorted_right)

result = sum(distance)

print(result)
