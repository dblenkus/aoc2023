import re


def make_map(file, mapping):
    mapped = []
    not_mapped = mapping[:]
    while line := file.readline().strip():
        destination, source, length = map(int, line.split())

        new_not_mapped = []
        for start, end in not_mapped:
            if end < source or source + length < start:
                new_not_mapped.append([start, end])
                continue

            if start < source:
                new_not_mapped.append([start, source])

            if source + length < end:
                new_not_mapped.append([source + length, end])

            mapped.append(
                [
                    destination + max(start, source) - source,
                    destination + min(end, source + length) - source,
                ]
            )

        not_mapped = new_not_mapped

    return mapped + not_mapped


with open("input.txt", "r") as file:
    seeds = re.findall(r"\d+", file.readline().strip())
    seeds = [int(seed) for seed in seeds]

    ranges = []
    while seeds:
        length = seeds.pop()
        start = seeds.pop()
        ranges.append([start, start + length])

    file.readline()
    for _ in range(7):
        file.readline()
        ranges = make_map(file, ranges)

    print(min([interval[0] for interval in ranges]))
