import re


def make_map(file, mapping):
    matches = []
    while line := file.readline().strip():
        numbers = re.findall(r"\d+", line)
        matches.append([int(n) for n in numbers])

    new_mapping = []
    for seed in mapping:
        for destination, source, length in matches:
            if seed >= source and seed < source + length:
                new_mapping.append(destination + seed - source)
                break
        else:
            new_mapping.append(seed)

    return new_mapping


with open("input.txt", "r") as file:
    seeds = re.findall(r"\d+", file.readline().strip())
    seeds = [int(seed) for seed in seeds]

    file.readline()
    for _ in range(7):
        file.readline()

        seeds = make_map(file, seeds)

    print(min(seeds))
