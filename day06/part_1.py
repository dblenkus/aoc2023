import re


result = 1
with open("input.txt", "r") as file:
    times = re.findall(r"\d+", file.readline().strip())
    distances = re.findall(r"\d+", file.readline().strip())

for time, distance in zip(times, distances):
    time = int(time)
    distance = int(distance)

    winning = 0
    for speed in range(time):
        if (time - speed) * speed > distance:
            winning += 1

    result *= winning

print(result)
