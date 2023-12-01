result = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        numbers = [int(char) for char in line if char.isdigit()]
        result += 10 * numbers[0] + numbers[-1]

print(result)
