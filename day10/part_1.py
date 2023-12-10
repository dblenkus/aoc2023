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
        return self.landscape[position.line][position.column]

    def __repr__(self):
        return "\n".join(["".join(line) for line in self.landscape])

    def find_start(self):
        for i, line in enumerate(self.landscape):
            if "S" in line:
                return Position(i, line.index("S"))


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
        self.start = landscape.find_start()
        self.position = self.start
        self.move = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.move is None:
            self.move = self.get_possible_move()
            return self.position

        self.position = self.position + self.move
        if self.position == self.start:
            raise StopIteration

        part = self.landscape[self.position]
        self.move = self.directions[part][self.move]
        return self.position

    def get_possible_move(self):
        for move in [Move.UP, Move.RIGHT, Move.DOWN, Move.LEFT]:
            if self.can_move(move):
                return move
        raise ValueError("Invalid start")

    def can_move(self, direction):
        part = self.landscape[self.position + direction]
        return Move.reverse(direction) in self.directions[part].values()


with open("input.txt", "r") as file:
    landscape = Landscape(file.readlines())

walk = Walk(landscape)
print(len(list(walk)) // 2)
