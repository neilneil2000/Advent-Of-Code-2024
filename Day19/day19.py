from functools import lru_cache
from day19_input import designs, towels

# from day19_input import designs_example as designs
# from day19_input import towels_example as towels


def chop_towel(towel, max_len):
    """Return list of towel segments if a split is possible"""
    for x in range(max_len, 0, -1):
        if towel[:x] not in designs:
            continue
        if not towel[x:]:
            return [towel[:x]]
        if next_segment := chop_towel(towel[x:], max_len):
            return [towel[:x]] + next_segment
    return []


@lru_cache()
def all_combos(towel, max_len):
    """Return all combinations of towel patterns"""
    total = 0
    for x in range(min(max_len, len(towel)), 0, -1):
        if towel[:x] not in designs:
            continue
        if not towel[x:]:
            total += 1
        if remainder := all_combos(towel[x:], max_len):
            total += remainder
    return total


def main():
    max_len = max(len(design) for design in designs)
    counter = sum(chop_towel(towel, max_len) != [] for towel in towels)
    print(f"Day 19 Part 1: {counter}")

    total = sum(all_combos(towel, max_len) for towel in towels)
    print(f"Day 19 Part 2: {total}")


if __name__ == "__main__":
    main()
