import math
import re

result = 0
with open("input.txt", "r") as file:
    for line in file:
        bag = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game_n = int(re.match(r"Game (\d+):", line).group(1))
        for match in re.finditer(r"(\d+) (red|green|blue)", line):
            bag[match[2]] = max(bag[match[2]], int(match[1]))

        result += math.prod(bag.values())

print(result)
