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


def main():
    max_len = max(len(design) for design in designs)
    counter = sum(chop_towel(towel, max_len) != [] for towel in towels)
    print(f"Day 19 Part 1: {counter}")


if __name__ == "__main__":
    main()
