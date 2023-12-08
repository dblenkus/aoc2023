from functools import reduce
import math
import re


class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.last = index % 26 == 25


graph = [None for _ in range(26**3)]


def get_node(string):
    index = reduce(lambda res, ch: res * 26 + ord(ch) - ord("A"), string, 0)
    if graph[index] is None:
        graph[index] = Node(index)
    return graph[index]


def get_shortest_path(node, instructions):
    result = 0
    while not node.last:
        instruction = instructions[result % len(instructions)]
        node = node.left if instruction == "L" else node.right
        result += 1
    return result


nodes = []
with open("input.txt", "r") as file:
    instructions = file.readline().strip()
    file.readline()

    for line in file:
        matches = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line.strip())
        start, left, right = matches.groups()

        if start[-1] == "A":
            nodes.append(get_node(start))

        start = get_node(start)
        start.left = get_node(left)
        start.right = get_node(right)

result = [get_shortest_path(node, instructions) for node in nodes]
print(math.lcm(*result))
