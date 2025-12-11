#!/usr/bin/env python3

from math import floor


def problem1() -> int:
    invalid_id_sum = 0
    with open("input.txt", "r") as file:
        for x in file.readline().split(","):
            start_str, stop_str = x.split("-")
            start, stop = int(start_str), int(stop_str)

            search_start = (
                int(start_str[: int(len(start_str) / 2)])
                if len(start_str) % 2 == 0
                else int("1" + "0" * floor(len(start_str) / 2))
            )

            invalid_ids = set()
            for pattern in range(
                search_start, stop
            ):  # Could calculate stop but we will break the loop in an optimal way anyway
                pattern_str = str(pattern)
                invalid_id = int(pattern_str + pattern_str)
                if invalid_id > stop:
                    break

                if start <= invalid_id:
                    invalid_ids.add(invalid_id)

            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum


def problem2() -> int:
    invalid_id_sum = 0
    with open("input.txt", "r") as file:
        for x in file.readline().split(","):
            start_str, stop_str = x.split("-")
            start, stop = int(start_str), int(stop_str)

            search_start = 1
            search_stop = (
                int(stop_str[: int(len(stop_str) / 2)])
                if len(stop_str) % 2 == 0
                else int("9" * floor(len(stop_str) / 2))
            )

            invalid_ids = set()
            for pattern in range(search_start, search_stop + 1):
                pattern_str = str(pattern)
                max_repeat = floor(len(stop_str) / len(pattern_str))
                for repeat in range(2, max(max_repeat + 1, 3)):
                    invalid_id = int(pattern_str * repeat)

                    if start <= invalid_id <= stop:
                        invalid_ids.add(invalid_id)

            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum


answer = problem2()
print(answer)
