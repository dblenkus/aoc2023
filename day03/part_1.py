with open("input.txt", "r") as file:
    input_ = file.readlines()

for i in range(len(input_)):
    input_[i] = '.' + input_[i].strip() + '.'

input_.insert(0, '.' * len(input_[0]))
input_.append('.' * len(input_[0]))

def is_part_number(line, start, end):
    around = set()

    around.add(input_[line][start-1])
    around.add(input_[line][end])

    around.update([*input_[line-1][start:end]])
    around.update([*input_[line+1][start:end]])

    around.add(input_[line-1][start-1])
    around.add(input_[line-1][end])
    around.add(input_[line+1][start-1])
    around.add(input_[line+1][end])

    around -= set([".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

    return len(around) > 0


result = 0
for i in range(len(input_)):
    start = 0
    for j in range(1, len(input_[i])):
        if not input_[i][j-1].isdigit() and input_[i][j].isdigit():
            start = j
        if input_[i][j-1].isdigit() and not input_[i][j].isdigit():
            if is_part_number(i, start, j):
                result += int(input_[i][start:j])

print(result)
