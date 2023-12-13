def find_reflection(pattern):
    for i in range(1, len(pattern)):
        up, down = pattern[:i], pattern[i:]
        up.reverse()
        for j in range(min(len(up), len(down))):
            if up[j] != down[j]:
                break
        else:
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
