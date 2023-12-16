from collections import defaultdict
from enum import Enum


class Direction(Enum):
    left = (0, -1)
    right = (0, 1)
    up = (-1, 0)
    down = (1, 0)


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __hash__(self):
        return hash((self.line, self.column))

    def __eq__(self, other):
        return self.line == other.line and self.column == other.column

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.line + other.line, self.column + other.column)
        elif isinstance(other, Direction):
            value = other.value
            return Position(self.line + value[0], self.column + value[1])

    def __repr__(self):
        return f"({self.line}, {self.column})"


class Layout:
    def __init__(self, layout):
        self.layout = [list(line.strip()) for line in layout]

    def __repr__(self):
        return "\n".join(["".join(line) for line in self.layout])

    def __getitem__(self, position):
        if isinstance(position, Position):
            return self.layout[position.line][position.column]
        elif isinstance(position, int):
            return self.layout[position]

    def inside(self, position):
        rows, columns = len(self.layout), len(self.layout[0])
        return 0 <= position.line < rows and 0 <= position.column < columns


class EnergizedLayout(Layout):
    def __init__(self, layout):
        self.layout = [["." for _ in line] for line in layout]

    def __setitem__(self, position, value):
        self.layout[position.line][position.column] = value

    def reset(self):
        self.layout = [["." for _ in line] for line in self.layout]

    def count_energy(self):
        result = 0
        for line in self.layout:
            result += line.count("#")
        return result


class Contraption:
    mapping = {
        ".": {
            Direction.up: [Direction.up],
            Direction.left: [Direction.left],
            Direction.down: [Direction.down],
            Direction.right: [Direction.right],
        },
        "/": {
            Direction.up: [Direction.right],
            Direction.left: [Direction.down],
            Direction.down: [Direction.left],
            Direction.right: [Direction.up],
        },
        "\\": {
            Direction.up: [Direction.left],
            Direction.left: [Direction.up],
            Direction.down: [Direction.right],
            Direction.right: [Direction.down],
        },
        "|": {
            Direction.up: [Direction.up],
            Direction.down: [Direction.down],
            Direction.left: [Direction.up, Direction.down],
            Direction.right: [Direction.up, Direction.down],
        },
        "-": {
            Direction.up: [Direction.left, Direction.right],
            Direction.down: [Direction.left, Direction.right],
            Direction.left: [Direction.left],
            Direction.right: [Direction.right],
        },
    }

    def __init__(self, layout):
        self.layout = Layout(layout)
        self.energized = EnergizedLayout(self.layout.layout)
        self.history = defaultdict(list)

    def move(self, position, direction):
        moves = [(position, direction)]
        while moves:
            position, direction = moves.pop()
            if direction in self.history[position]:
                continue
            self.history[position].append(direction)
            self.energized[position] = "#"

            for new_direction in self.mapping[self.layout[position]][direction]:
                new_position = position + new_direction
                if self.layout.inside(new_position):
                    moves.append((new_position, new_direction))


with open("input.txt", "r") as file:
    contraption = Contraption(file.readlines())

contraption.move(Position(0, 0), Direction.right)

result = 0
for line in contraption.energized:
    result += line.count("#")

print(result)
