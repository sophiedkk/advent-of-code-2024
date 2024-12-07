from itertools import cycle
from pathlib import Path

map_grid = [list(line) for line in Path("data/day_06.txt").read_text().splitlines()]

starting_position = [0, 0]
for y, line in enumerate(map_grid):
    for x, pos in enumerate(line):
        if pos == "^":
            starting_position = [x, y]


class Guard:
    def __init__(self, x_pos, y_pos, grid, orientation):
        self.x = x_pos
        self.y = y_pos
        self.grid = grid
        self.orientation = orientation
        self.orientations = cycle(["UP", "RIGHT", "DOWN", "LEFT"])
        self.grid[self.y][self.x] = "X"  # Mark starting position

        while self.orientation != next(self.orientations):
            pass

    def move(self) -> bool:
        next_x, next_y = self.x, self.y
        match self.orientation:
            case "UP":
                next_y = self.y - 1
            case "RIGHT":
                next_x = self.x + 1
            case "DOWN":
                next_y = self.y + 1
            case "LEFT":
                next_x = self.x - 1
        if next_y < 0 or next_y >= len(self.grid) or next_x < 0 or next_x >= len(self.grid[0]):  # noqa
            return False

        if self.grid[next_y][next_x] == "#":
            self.rotate()
        else:
            self.x, self.y = next_x, next_y
            self.grid[self.y][self.x] = "X"
        return True

    def rotate(self):
        self.orientation = next(self.orientations)

    def show_grid(self):
        for line in self.grid:
            print("".join(line))
        print()


guard = Guard(starting_position[0], starting_position[1], map_grid, "UP")

while guard.move():
    guard.show_grid()

sum(line.count("X") for line in guard.grid)
