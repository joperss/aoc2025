#!/usr/bin/env python3


def problem1() -> int:
    accessible_rolls = 0
    grid: list[list[str]] = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = [char for char in line]
            grid.append(row)

        y_max = len(grid) - 1
        x_max = len(grid[0]) - 1

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "@":
                    neighbors = 0
                    if y > 0:
                        if x > 0:
                            neighbors += grid[y - 1][x - 1] == "@"

                        neighbors += grid[y - 1][x] == "@"

                        if x < x_max:
                            neighbors += grid[y - 1][x + 1] == "@"

                    if x > 0:
                        neighbors += grid[y][x - 1] == "@"
                    if x < x_max:
                        neighbors += grid[y][x + 1] == "@"

                    if y < y_max:
                        if x > 0:
                            neighbors += grid[y + 1][x - 1] == "@"

                        neighbors += grid[y + 1][x] == "@"

                        if x < x_max:
                            neighbors += grid[y + 1][x + 1] == "@"
                    if neighbors < 4:
                        accessible_rolls += 1

    return accessible_rolls


def problem2() -> int:
    accessible_rolls: list[tuple[int, int]] = []
    grid: list[list[str]] = []
    with open("test_input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = [char for char in line]
            grid.append(row)

        y_max = len(grid) - 1
        x_max = len(grid[0]) - 1

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == "@":
                    neighbors = 0
                    if y > 0:
                        if x > 0:
                            neighbors += grid[y - 1][x - 1] == "@"

                        neighbors += grid[y - 1][x] == "@"

                        if x < x_max:
                            neighbors += grid[y - 1][x + 1] == "@"

                    if x > 0:
                        neighbors += grid[y][x - 1] == "@"
                    if x < x_max:
                        neighbors += grid[y][x + 1] == "@"

                    if y < y_max:
                        if x > 0:
                            neighbors += grid[y + 1][x - 1] == "@"

                        neighbors += grid[y + 1][x] == "@"

                        if x < x_max:
                            neighbors += grid[y + 1][x + 1] == "@"
                    if neighbors < 4:
                        accessible_rolls.append((x, y))

    return len(accessible_rolls)


answer = problem2()
print("Answer: ", answer)
assert answer == 43
