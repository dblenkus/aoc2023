from enum import Enum


class Move(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    @classmethod
    def reverse(cls, move):
        mapping = {
            cls.UP: cls.DOWN,
            cls.DOWN: cls.UP,
            cls.LEFT: cls.RIGHT,
            cls.RIGHT: cls.LEFT,
        }
        return mapping[move]


class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __eq__(self, other):
        return self.line == other.line and self.column == other.column

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.line + other.line, self.column + other.column)
        elif isinstance(other, Move):
            value = other.value
            return Position(self.line + value[0], self.column + value[1])

    def __repr__(self):
        return f"({self.line}, {self.column})"


class Landscape:
    def __init__(self, landscape):
        self.landscape = ["." + line + "." for line in landscape]
        self.landscape.insert(0, "." * len(self.landscape[0]))
        self.landscape.append("." * len(self.landscape[0]))

    def __getitem__(self, position):
        if isinstance(position, Position):
            return self.landscape[position.line][position.column]
        elif isinstance(position, int):
            return self.landscape[position]

    def __setitem__(self, position, value):
        line = self.landscape[position.line]
        new_line = line[: position.column] + value + line[position.column + 1 :]
        self.landscape[position.line] = new_line

    def __repr__(self):
        return "\n".join(["".join(line) for line in self.landscape])

    def find_start(self):
        for i, line in enumerate(self.landscape):
            if "S" in line:
                return Position(i, line.index("S"))

    def get_size(self):
        return len(self.landscape), len(self.landscape[0])

    def count_inside(self):
        result = 0
        for line in self.landscape:
            inside = False
            previous = None
            for char in line:
                if char == "." and inside:
                    result += 1
                if char in ["F", "L", "7", "J"]:
                    if not previous:
                        previous = char
                    else:
                        if (char == "7" and previous == "L") or (
                            char == "J" and previous == "F"
                        ):
                            inside = not inside
                        previous = None
                if char == "|":
                    inside = not inside
        return result

    @classmethod
    def get_empty(cls, lines, columns):
        return cls(["." * columns for _ in range(lines)])


class Walk:
    directions = {
        "|": {Move.UP: Move.UP, Move.DOWN: Move.DOWN},
        "7": {Move.RIGHT: Move.DOWN, Move.UP: Move.LEFT},
        "F": {Move.UP: Move.RIGHT, Move.LEFT: Move.DOWN},
        "-": {Move.RIGHT: Move.RIGHT, Move.LEFT: Move.LEFT},
        "L": {Move.DOWN: Move.RIGHT, Move.LEFT: Move.UP},
        "J": {Move.DOWN: Move.LEFT, Move.RIGHT: Move.UP},
    }

    def __init__(self, landscape):
        self.landscape = landscape
        self.visited = Landscape.get_empty(*landscape.get_size())
        self.start = landscape.find_start()
        self.position = self.start
        self.move = None
        self.replace_start()

    def __iter__(self):
        return self

    def __next__(self):
        if self.move is None:
            self.move = self.get_possible_move()
            return self.position

        self.change_position(self.position + self.move)
        if self.position == self.start:
            raise StopIteration

        return self.position

    def replace_start(self):
        for part, mapping in self.directions.items():
            if self.can_move(*mapping.values(), position=self.start):
                self.landscape[self.start] = part
                break
        else:
            raise ValueError("Invalid start")

    def get_possible_move(self):
        for move in [Move.UP, Move.RIGHT, Move.DOWN, Move.LEFT]:
            if self.can_move(move):
                return move
        raise ValueError("Invalid start")

    def can_move(self, *directions, position=None):
        position = position or self.position
        for direction in directions:
            part = self.landscape[position + direction]
            if Move.reverse(direction) not in self.directions[part].values():
                return False
        return True

    def change_position(self, position):
        self.position = position
        self.visited[position] = self.landscape[position]
        part = self.landscape[self.position]
        self.move = self.directions[part][self.move]

    def run(self):
        list(self)

    def get_visited(self):
        return self.visited


with open("input.txt", "r") as file:
    landscape = Landscape(file.readlines())

walk = Walk(landscape)
walk.run()
print(walk.get_visited().count_inside())
