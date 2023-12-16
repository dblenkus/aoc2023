with open("input.txt", "r") as file:
    input_ = file.readlines()

for i in range(len(input_)):
    input_[i] = '.' + input_[i].strip() + '.'

input_.insert(0, '.' * len(input_[0]))
input_.append('.' * len(input_[0]))

gears = []
for i in range(len(input_)):
    gears.append([0]*len(input_[i]))

parts = []
for i in range(len(input_)):
    parts.append([[] for _ in range(len(input_[i]))])


def is_gear(i, j):
    around = set()

    around.add(gears[i][j-1])
    around.add(gears[i][j+1])

    around.update([*gears[i-1][j-1:j+2]])
    around.update([*gears[i+1][j-1:j+2]])

    around.discard(0)

    return len(around) == 2


def update_parts(line, start, end):
    part = int(input_[line][start:end])
    for i in range(start-1, end+1):
        parts[line-1][i].append(part)
        parts[line+1][i].append(part)
    parts[line][start-1].append(part)
    parts[line][end].append(part)


result = 0
gear = 1
for i in range(len(input_)):
    start = 0
    for j in range(1, len(input_[i])):
        if not input_[i][j-1].isdigit() and input_[i][j].isdigit():
            start = j
        if input_[i][j].isdigit():
            gears[i][j] = gear
        if input_[i][j-1].isdigit() and not input_[i][j].isdigit():
            gear += 1
            update_parts(i, start, j)

for i in range(len(input_)):
    for j in range(1, len(input_[i])):
        if input_[i][j] == "*" and is_gear(i, j):
            result += parts[i][j][0] * parts[i][j][1]

print(result)
