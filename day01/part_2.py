class TreeNode:
    def __init__(self, prefix, value=None, children=None):
        self.prefix = prefix
        self.value = value
        self.children = children or []

    @property
    def is_leaf(self):
        return len(self.children) == 0

    def search(self, line, index):
        if index + len(self.prefix) > len(line):
            return None

        for i in range(len(self.prefix)):
            if line[index + i] != self.prefix[i]:
                return None

        if self.is_leaf:
            return self.value

        for child in self.children:
            value = child.search(line, index + len(self.prefix))
            if value is not None:
                return value


tree = TreeNode(
    "",
    children=[
        TreeNode("1", value=1),
        TreeNode("2", value=2),
        TreeNode("3", value=3),
        TreeNode("4", value=4),
        TreeNode("5", value=5),
        TreeNode("6", value=6),
        TreeNode("7", value=7),
        TreeNode("8", value=8),
        TreeNode("9", value=9),
        TreeNode("one", value=1),
        TreeNode(
            "t",
            children=[
                TreeNode("wo", value=2),
                TreeNode("hree", value=3),
            ],
        ),
        TreeNode(
            "f",
            children=[
                TreeNode("our", value=4),
                TreeNode("ive", value=5),
            ],
        ),
        TreeNode(
            "s",
            children=[
                TreeNode("ix", value=6),
                TreeNode("even", value=7),
            ],
        ),
        TreeNode("eight", value=8),
        TreeNode("nine", value=9),
    ],
)

result = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        for i in range(len(line)):
            first = tree.search(line, i)
            if first is not None:
                break

        for i in range(len(line) - 1, -1, -1):
            last = tree.search(line, i)
            if last is not None:
                break

        result += 10 * first + last

print(result)
