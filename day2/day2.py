#!/usr/bin/env python3

from math import floor


def problem1() -> int:
    with open("input.txt", "r") as file:
        invalid_id_sum = 0
        for x in file.readline().split(","):
            start_str, stop_str = x.split("-")
            start = int(start_str)
            stop = int(stop_str)

            search_start = (
                int(start_str[: int(len(start_str) / 2)])
                if len(start_str) % 2 == 0
                else int("1" + "0" * floor(len(start_str) / 2))
            )
            for i in range(search_start, stop):
                i_str = str(i)
                invalid_id = int(i_str + i_str)
                if invalid_id > stop:
                    break

                if invalid_id >= start:
                    invalid_id_sum += invalid_id
    return invalid_id_sum


def problem2() -> int:
    with open("input.txt", "r") as file:
        invalid_id_sum = 0
        for x in file.readline().split(","):
            start_str, stop_str = x.split("-")
            start = int(start_str)
            stop = int(stop_str)

            search_stop = (
                int(stop_str[: int(len(stop_str) / 2)])
                if len(stop_str) % 2 == 0
                else int("9" * int((len(stop_str) - 1) / 2))
            )
            invalid_ids = set()
            for i in range(1, search_stop + 1):
                max_repeat = floor(len(stop_str) / len((str(i))))
                for j in range(2, max_repeat + 1 if max_repeat > 2 else 3):
                    if start <= int(str(i) * j) <= stop:
                        invalid_ids.add(int(str(i) * j))
            invalid_id_sum += sum(invalid_ids)

    return invalid_id_sum


answer = problem2()
print("Invalid ID sum: " + str(answer))
