def find_reflection(pattern):
    for i in range(len(pattern)):
        up, down = pattern[:i], pattern[i:]
        up.reverse()
        different = 0
        for j in range(min(len(up), len(down))):
            for k in range(len(up[0])):
                if up[j][k] != down[j][k]:
                    different += 1
        if different == 1:
            return i
    return 0


patterns = [[]]
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            patterns[-1].append(line)
        else:
            patterns.append([])

result = 0
for pattern in patterns:
    result += 100 * find_reflection(pattern)
    transposed = list(zip(*pattern))
    result += find_reflection(transposed)


print(result)
