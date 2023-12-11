space = []
with open("input.txt", "r") as file:
    for line in file:
        space.append(line.strip())


for i in range(len(space) - 1, 0, -1):
    if all([char == "." for char in space[i]]):
        space.insert(i, "." * len(space[0]))

for i in range(len(space[0]) - 1, 0, -1):
    if all([line[i] == "." for line in space]):
        for j in range(len(space)):
            space[j] = space[j][:i] + "." + space[j][i:]

galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j] == "#":
            galaxies.append((i, j))

result = 0
for first in galaxies:
    for second in galaxies:
        result += abs(first[0] - second[0]) + abs(first[1] - second[1])

print(result // 2)
