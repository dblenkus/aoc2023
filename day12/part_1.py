result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        condition, groups = line.split(" ")
        groups = [int(number) for number in groups.split(",")]

        gaps = [[]]
        for i in range(len(groups) + 1):
            new_gaps = []
            for j in range(len(condition) - sum(groups) + 1):
                new_gaps.extend([gap + [j] for gap in gaps])

            gaps = new_gaps

        correct_gaps = []
        for gap in gaps:
            if sum(gap) + sum(groups) != len(condition):
                continue
            if any(space == 0 for space in gap[1:-1]):
                continue

            correct_gaps.append(gap)

        for gap in correct_gaps:
            arrangement = "." * gap[0]
            for i in range(len(groups)):
                arrangement += "#" * groups[i]
                arrangement += "." * gap[i + 1]

            for i in range(len(condition)):
                if condition[i] == "?":
                    continue
                if condition[i] != arrangement[i]:
                    break
            else:
                result += 1

print(result)
