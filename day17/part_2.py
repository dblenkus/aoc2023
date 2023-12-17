import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def possible_directions(direction, straight):
    directions = [0, 1, 2, 3]
    directions.remove((direction + 2) % 4)
    if straight != 0 and straight < 4:
        directions = [direction]
    elif straight == 10:
        directions.remove(direction)
    return directions


def search(city):
    visited = set()
    heatlosses = {}
    queue = []
    heapq.heappush(queue, (0, (0, 0, 0, 0)))
    while len(queue) > 0:
        heatloss, position = heapq.heappop(queue)
        y, x, direction, straight = position
        if position in visited:
            continue
        visited.add(position)

        for new_direction in possible_directions(direction, straight):
            new_y = y + DIRECTIONS[new_direction][0]
            new_x = x + DIRECTIONS[new_direction][1]
            if new_y < 0 or len(city) <= new_y or new_x < 0 or len(city[0]) <= new_x:
                continue

            new_heatloss = city[new_y][new_x] + heatloss
            new_straight = straight + 1 if new_direction == direction else 1
            new_position = (new_y, new_x, new_direction, new_straight)
            if (
                new_position not in heatlosses
                or new_heatloss < heatlosses[new_position]
            ):
                heatlosses[new_position] = new_heatloss
                heapq.heappush(queue, (new_heatloss, new_position))

    return heatlosses


city = []
with open("input.txt", "r") as file:
    for line in file:
        city.append([int(number) for number in line.strip()])


heatlosses = search(city)

result = None
for position, heatloss in heatlosses.items():
    if position[0] == len(city) - 1 and position[1] == len(city[0]) - 1:
        if result is None or heatloss < result:
            result = heatloss

print(result)
