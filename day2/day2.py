#!/usr/bin/env python3

with open("input.txt", "r") as file:
    invalid_id_count = 0
    for x in file.readline().split(","):
        start, stop = x.split("-")

        for i in range(int(start), int(stop) + 1):
            i_str = str(i)
            i_len = len(i_str)
            if i_len % 2 != 0:
                pass

            pre = i_str[: int(i_len / 2)]
            post = i_str[int(i_len / 2) :]
            if pre == post:
                invalid_id_count += i

    print("Invalid ID count: " + str(invalid_id_count))
