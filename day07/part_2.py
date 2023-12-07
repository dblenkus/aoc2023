from collections import Counter


def replace_labels(hand):
    mapping = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    return [mapping[card] if card in mapping else int(card) for card in hand]


def get_type(hand):
    counter = Counter(hand)
    max_cards = max(counter.values())

    if max_cards == 5:
        return 7  # Five of a kind.
    if max_cards == 4:
        return 6  # Four of a kind.
    if max_cards == 3:
        if len(counter) == 2:
            return 5  # Full house.
        return 4  # Three of a kind.
    if len(counter) == 3:
        return 3  # Two pair.
    if len(counter) == 4:
        return 2  # One pair.
    return 1  # High card.


def get_strongest_type(hand):
    if 1 not in hand:
        return get_type(hand)

    max_type = 0
    for joker in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]:
        new_type = get_type([joker if card == 1 else card for card in hand])
        max_type = max(max_type, new_type)
    return max_type


hands = []
with open("input.txt", "r") as file:
    for line in file:
        hand, bid = line.strip().split(" ")
        hand = replace_labels(hand)
        hands.append((get_strongest_type(hand), hand, int(bid)))

result = 0
for i, hand in enumerate(sorted(hands), start=1):
    result += hand[2] * i

print(result)
