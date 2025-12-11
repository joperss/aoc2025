#!/usr/bin/env python3


def problem1() -> int:
    total_capacity = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()

            bank = [x for x in line]
            max_capacity_candidate = set()
            for i, capacity_1 in enumerate(bank):
                for capacity_2 in bank[i + 1 :]:
                    max_capacity_candidate.add(int(capacity_1 + capacity_2))
            max_bank_capacity = max(max_capacity_candidate)
            total_capacity += max_bank_capacity

    return total_capacity


def problem2() -> int:
    total_capacity = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()

            bank = [int(x) for x in line]
            max_capacity = find_max_capacity("", bank, 12)
            total_capacity += max_capacity

    return total_capacity


def find_max_capacity(capacaties: str, candidates: list[int], remaining_choices) -> int:
    if remaining_choices == 0:
        return int(capacaties)

    chosen_battery: tuple[int, int] = (0, -1)
    for i, capacity in enumerate(
        candidates[0 : len(candidates) - remaining_choices + 1]
    ):
        if capacity > chosen_battery[0]:
            chosen_battery = (capacity, i)

    return find_max_capacity(
        capacaties + str(chosen_battery[0]),
        candidates[chosen_battery[1] + 1 :],
        remaining_choices - 1,
    )


answer = problem2()
print("Max capacity: ", answer)
# assert answer == 3121910778619
