import re


def parse_numbers(numbers):
    return {int(number) for number in re.split(r"\s+", numbers.strip())}


result = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        _, numbers = line.split(":")
        your_numbers, winning_numbers = numbers.split("|")

        your_numbers = parse_numbers(your_numbers)
        winning_numbers = parse_numbers(winning_numbers)

        intersection = your_numbers.intersection(winning_numbers)

        if intersection:
            result += 2 ** (len(intersection) - 1)

print(result)
