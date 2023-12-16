import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

result = 0
with open("input.txt", "r") as file:
    number = 0
    for line in file:
        game_n = int(re.match(r"Game (\d+):", line).group(1))
        for match in re.finditer(r"(\d+) (red|green|blue)", line):
            if bag[match[2]] < int(match[1]):
                break
        else:
            result += int(game_n)

print(result)
