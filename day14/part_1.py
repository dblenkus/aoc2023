with open("input.txt", "r") as file:
    platform = [line.strip() for line in file]

result = 0
for column in range(len(platform[0])):
    empty_position = None
    for row in range(len(platform)):
        if platform[row][column] == "." and empty_position is None:
            empty_position = row
        elif platform[row][column] == "#":
            empty_position = None
        elif platform[row][column] == "O":
            if empty_position is not None:
                result += len(platform) - empty_position
                empty_position += 1
            else:
                result += len(platform) - row

print(result)
