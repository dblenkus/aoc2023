from functools import reduce
import re


class Node:
    def __init__(self):
        self.left = None
        self.right = None


graph = [None for _ in range(26**3)]


def get_node(string):
    index = reduce(lambda res, ch: res * 26 + ord(ch) - ord("A"), string, 0)
    if graph[index] is None:
        graph[index] = Node()
    return graph[index]


with open("input.txt", "r") as file:
    instructions = file.readline().strip()
    file.readline()

    for line in file:
        matches = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line.strip())
        start, left, right = matches.groups()

        start = get_node(start)
        start.left = get_node(left)
        start.right = get_node(right)

result = 0
node = graph[0]
while node != graph[-1]:
    instruction = instructions[result % len(instructions)]
    node = node.left if instruction == "L" else node.right
    result += 1

print(result)
