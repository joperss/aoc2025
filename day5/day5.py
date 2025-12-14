#!/usr/bin/env python3


from re import T
import re
from typing import Self


def problem1() -> int:
    with open("input.txt", "r") as file:
        ranges = set()
        fresh = 0
        for line in file:
            line = line.strip()
            if "-" in line:
                parts = line.split("-")
                ranges.add((int(parts[0]), int(parts[1])))
            elif line:
                for low, high in ranges:
                    if low <= int(line) <= high:
                        fresh += 1
                        break

    return fresh


class Range:
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    def __contains__(self, item: Self):
        return item.lower <= self.upper and item.upper >= self.lower

    def __str__(self) -> str:
        return str(self.lower) + "-" + str(self.upper)

    def extend(self, item: Self):
        if item not in self:
            assert False
        if item.lower < self.lower:
            self.lower = item.lower
        if item.upper > self.upper:
            self.upper = item.upper


def problem2() -> int:
    with open("input.txt", "r") as file:
        ranges = set()
        for line in file:
            line = line.strip()
            if "-" in line:
                lower, upper = line.split("-")
                lower, upper = int(lower), int(upper)
                range = Range(lower, upper)
                overlaps = set()
                for existing in ranges:
                    if range in existing:
                        overlaps.add(existing)

                for existing in overlaps:
                    ranges.remove(existing)
                    range.extend(existing)

                ranges.add(range)

    fresh_id_count = 0
    for range in ranges:
        fresh_id_count += range.upper - range.lower + 1

    return fresh_id_count


answer = problem2()
print("Answer: ", answer)
# assert answer == 14
