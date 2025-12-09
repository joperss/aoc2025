#!/usr/bin/env python3


class Node:
    def __init__(self, data, prev, next) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class Dial:
    def __init__(self, start, stop, start_pos) -> None:
        self.head: Node = Node(start, None, None)
        self.curr: Node = self.head
        for i in range(start + 1, stop):
            node = Node(i, self.curr, None)
            self.curr.next = node
            self.curr = node

        node = Node(stop, self.curr, self.head)
        self.curr.next = node
        self.head.prev = node
        self.curr = self.head

        self.step(start_pos, "L")

    def step(self, steps, dir):
        if dir == "L":
            while steps > 0:
                self.curr = self.curr.next
                steps -= 1
        elif dir == "R":
            while steps > 0:
                self.curr = self.curr.prev
                steps -= 1


dial = Dial(0, 99, 50)
code = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        dir = line[0]
        steps = int(line[1:])
        dial.step(steps, dir)
        if dial.curr.data == 0:
            code += 1

print(code)
