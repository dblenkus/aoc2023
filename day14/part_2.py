class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return f"({self.row}, {self.column})"

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.row, self.column))


class Rock:
    def __init__(self, coordinate, weight):
        self.coordinate = coordinate
        self.weight = weight

    def __repr__(self):
        return f"Rock(position={self.coordinate}, weight={self.weight})"

    def __eq__(self, other):
        return self.coordinate == other.coordinate

    def __hash__(self):
        return hash(self.coordinate)


class Platform:
    def __init__(self, platform):
        self.platform = [list(line.strip()) for line in platform]

    def __getitem__(self, coordinate):
        return self.platform[coordinate.row][coordinate.column]

    def __setitem__(self, coordinate, value):
        self.platform[coordinate.row][coordinate.column] = value

    def __repr__(self):
        return "\n".join("".join(row) for row in self.platform)

    def _move(self, iterator):
        empty_spaces = []
        for coordinate, switch in iterator:
            if switch:
                empty_spaces = []

            if self[coordinate] == ".":
                empty_spaces.append(coordinate)
            elif self[coordinate] == "#":
                empty_spaces = []
            elif self[coordinate] == "O" and empty_spaces:
                self[empty_spaces.pop(0)] = "O"
                self[coordinate] = "."
                empty_spaces.append(coordinate)

    def north(self):
        self._move(
            (
                (Coordinate(row, column), row == 0)
                for column in range(len(self.platform[0]))
                for row in range(len(self.platform))
            )
        )

    def west(self):
        self._move(
            (
                (Coordinate(row, column), column == 0)
                for row in range(len(self.platform))
                for column in range(len(self.platform[0]))
            )
        )

    def south(self):
        self._move(
            (
                (Coordinate(row, column), row == len(self.platform) - 1)
                for column in range(len(self.platform[0]))
                for row in range(len(self.platform) - 1, -1, -1)
            )
        )

    def east(self):
        self._move(
            (
                (Coordinate(row, column), column == len(self.platform[0]) - 1)
                for row in range(len(self.platform))
                for column in range(len(self.platform[0]) - 1, -1, -1)
            )
        )

    def spin(self):
        self.north()
        self.west()
        self.south()
        self.east()

    def find_rocks(self):
        positions = (
            Coordinate(row, column)
            for column in range(len(self.platform[0]))
            for row in range(len(self.platform))
        )
        return set(
            Rock(position, len(self.platform) - position.row)
            for position in positions
            if self[position] == "O"
        )


with open("input.txt", "r") as file:
    platform = Platform(file.readlines())

positions = []
while (position := platform.find_rocks()) not in positions:
    positions.append(position)
    platform.spin()

index = positions.index(position)
interval = len(positions) - index
final_position = positions[(1000000000 - index) % interval + index]
print(sum(rock.weight for rock in final_position))
