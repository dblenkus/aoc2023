from itertools import zip_longest
import re


def parse_numbers(numbers):
    return {int(number) for number in re.split(r"\s+", numbers.strip())}


result = 0
cards = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        card, numbers = line.split(":")
        your_numbers, winning_numbers = numbers.split("|")

        card_number = int(re.search(r"\d+", card).group(0))

        your_numbers = parse_numbers(your_numbers)
        winning_numbers = parse_numbers(winning_numbers)

        intersection = your_numbers.intersection(winning_numbers)

        cards = cards + [1] * (len(intersection) - len(cards) + 1)
        current_card = cards.pop(0)
        new_cards = [current_card] * len(intersection)
        cards = list(map(sum, zip_longest(cards, new_cards, fillvalue=0)))

        result += current_card

print(result)
