#!/usr/bin/env python3

with open("input.txt", "r") as file:
    for x in file.readline().split(","):
        start, stop = x.split("-")
        print(start, stop)
