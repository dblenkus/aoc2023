def get_set(first, second):
    return set(range(min(second, first), max(second, first)))


space = []
with open("input.txt", "r") as file:
    for line in file:
        space.append(line.strip())

empty_lines = get_set(0, len(space))
empty_columns = get_set(0, len(space[0]))
galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            empty_lines.discard(i)
            empty_columns.discard(j)
            galaxies.append((i, j))

result = 0
for i, first in enumerate(galaxies):
    for second in galaxies[i:]:
        lines = get_set(first[0], second[0])
        columns = get_set(first[1], second[1])

        result += len(lines) + len(columns)
        result += 999999 * len(lines.intersection(empty_lines))
        result += 999999 * len(columns.intersection(empty_columns))

print(result)
