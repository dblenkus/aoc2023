import math
import re


def parse_number(string):
    return int(re.search(r"\d+", string.strip().replace(" ", "")).group())


with open("input.txt", "r") as file:
    time = parse_number(file.readline())
    distance = parse_number(file.readline())

a, b, c = 1, -time, distance
d = b**2 - 4 * a * c

x1 = (-b - math.sqrt(d)) / (2 * a)
x2 = (-b + math.sqrt(d)) / (2 * a)

print(math.floor(x2) - math.ceil(x1) + 1)
