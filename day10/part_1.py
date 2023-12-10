import math


with open("input.txt", "r") as file:
    landscape = file.readlines()

for i in range(len(landscape)):
    landscape[i] = '.' + landscape[i].strip() + '.'

landscape.insert(0, '.' * len(landscape[0]))
landscape.append('.' * len(landscape[0]))

for i, line in enumerate(landscape):
    if "S" in line:
        start = (i, line.index("S"))

if landscape[start[0]-1][start[1]] in ["|", "7", "F"]:
    direction = 1
    position = (start[0]-1, start[1])
elif landscape[start[0]+1][start[1]] in ["|", "J", "L"]:
    direction = 2
    position = (start[0]+1, start[1])
elif landscape[start[0]][start[1]-1] in ["-", "L", "F"]:
    direction = 3
    position = (start[0], start[1]-1)
elif landscape[start[0]][start[1]+1] in ["-", "J", "7"]:
    direction = 4
    position = (start[0], start[1]+1)

i = 0
while position != start:
    i += 1
    if direction == 1:
        if landscape[position[0]][position[1]] == "|":
            position = (position[0]-1, position[1])
        elif landscape[position[0]][position[1]] == "7":
            position = (position[0], position[1]-1)
            direction = 3
        elif landscape[position[0]][position[1]] == "F":
            position = (position[0], position[1]+1)
            direction = 4
    elif direction == 2:
        if landscape[position[0]][position[1]] == "|":
            position = (position[0]+1, position[1])
        elif landscape[position[0]][position[1]] == "J":
            position = (position[0], position[1]-1)
            direction = 3
        elif landscape[position[0]][position[1]] == "L":
            position = (position[0], position[1]+1)
            direction = 4
    elif direction == 3:
        if landscape[position[0]][position[1]] == "-":
            position = (position[0], position[1]-1)
        elif landscape[position[0]][position[1]] == "L":
            position = (position[0]-1, position[1])
            direction = 1
        elif landscape[position[0]][position[1]] == "F":
            position = (position[0]+1, position[1])
            direction = 2
    elif direction == 4:
        if landscape[position[0]][position[1]] == "-":
            position = (position[0], position[1]+1)
        elif landscape[position[0]][position[1]] == "J":
            position = (position[0]-1, position[1])
            direction = 1
        elif landscape[position[0]][position[1]] == "7":
            position = (position[0]+1, position[1])
            direction = 2

print(math.ceil(i/2))
