result = 0
with open("input.txt", "r") as file:
    for line in file:
        numbers = [int(number) for number in line.strip().split()]

        while any(numbers):
            result += numbers[-1]
            numbers = [b - a for a, b in zip(numbers, numbers[1:])]

print(result)
