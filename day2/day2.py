#!/usr/bin/env python3

with open("input.txt", "r") as file:
    invalid_id_count = 0
    for x in file.readline().split(","):
        start, stop = x.split("-")
        start = int(start)
        stop = int(stop)

        for i in range(1, stop):
            i_str = str(i)
            invalid_id = int(i_str + i_str)
            if invalid_id > stop:
                break

            if invalid_id >= start:
                invalid_id_count += invalid_id

    print("Invalid ID count: " + str(invalid_id_count))
