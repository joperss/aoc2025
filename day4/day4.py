#!/usr/bin/env python3


def problem1() -> int:
    grid: list[list[str]] = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = [char for char in line]
            grid.append(row)

        return len(find_accessible_rolls(grid))


def problem2() -> int:
    total_accessible_rolls = 0
    accessible_rolls: list[tuple[int, int]] = []
    grid: list[list[str]] = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            row = [char for char in line]
            grid.append(row)

        while True:
            accessible_rolls = find_accessible_rolls(grid)
            if len(accessible_rolls) == 0:
                break

            total_accessible_rolls += len(accessible_rolls)
            for x, y in accessible_rolls:
                grid[y][x] = "."

    return total_accessible_rolls


def find_accessible_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    accessible_rolls: list[tuple[int, int]] = []
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
    return accessible_rolls


answer = problem2()
print("Answer: ", answer)
# assert answer == 43
