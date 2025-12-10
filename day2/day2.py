#!/usr/bin/env python3

from math import floor

with open("input.txt", "r") as file:
    invalid_id_count = 0
    for x in file.readline().split(","):
        start_str, stop_str = x.split("-")
        start = int(start_str)
        stop = int(stop_str)

        search_start_str = (
            start_str[: int(len(start_str) / 2)]
            if len(start_str) % 2 == 0
            else "1" + "0" * floor(len(start_str) / 2)
        )
        for i in range(int(search_start_str), stop):
            i_str = str(i)
            invalid_id = int(i_str + i_str)
            if invalid_id > stop:
                break

            if invalid_id >= start:
                invalid_id_count += invalid_id

    print("Invalid ID count: " + str(invalid_id_count))
