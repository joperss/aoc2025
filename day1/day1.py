#!/usr/bin/env python3


class Node:
    def __init__(self, data: int, prev, next) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class Dial:
    def __init__(self, start: int, stop: int, start_pos: int) -> None:
        self.head = Node(start, None, None)
        self.curr = self.head
        for i in range(start + 1, stop):
            node = Node(i, self.curr, None)
            self.curr.next = node
            self.curr = node

        node = Node(stop, self.curr, self.head)
        self.curr.next = node
        self.head.prev = node
        self.curr = self.head

        self.step(start_pos, "R")

    def step(self, steps, dir) -> tuple[int, int]:
        zero_count = 0
        if dir == "L":
            while steps > 0:
                self.curr = self.curr.prev
                if self.curr.data == 0:
                    zero_count += 1
                steps -= 1
        elif dir == "R":
            while steps > 0:
                self.curr = self.curr.next
                if self.curr.data == 0:
                    zero_count += 1
                steps -= 1
        return self.curr.data, zero_count


def problem1() -> int:
    dial = Dial(0, 99, 50)
    code = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            dir = line[0]
            steps = int(line[1:])
            pos, _ = dial.step(steps, dir)
            if pos == 0:
                code += 1

    return code


def problem2() -> int:
    dial = Dial(0, 99, 50)
    code = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            dir = line[0]
            steps = int(line[1:])
            _, zero_count = dial.step(steps, dir)
            code += zero_count

    return code


print(problem2())
