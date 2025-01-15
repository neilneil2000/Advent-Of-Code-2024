from typing import List
from day2_input import DAY_2_INPUT


def main() -> None:

    reports = [list(map(int, entry.split())) for entry in DAY_2_INPUT.splitlines()]

    # diffs = [get_diff(report) for report in data]
    safe = [is_safe(report) for report in reports]
    print(f"Day 2 Part 1: {sum(safe)}")

    unsafe = [x[1] for x in zip(safe, reports) if not x[0]]
    semi_safe = [is_semi_safe(report) for report in unsafe]
    print(f"Day 2 Part 2: {sum(safe) + sum(semi_safe)}")


def get_diff(report: List) -> List:
    """Return list of differences between integers in list"""
    return list(map(lambda x, y: y - x, report[:-1], report[1:]))


def is_safe(report: List) -> List:
    """True if report is safe"""
    return all(0 < i <= 3 for i in get_diff(report)) or all(
        -3 <= i < 0 for i in get_diff(report)
    )


def is_semi_safe(report: List) -> List:
    """True is report is safe with a single element removed"""
    variants = [report[:i] + report[i + 1 :] for i in range(len(report))]
    return any(is_safe(variant) for variant in variants)


if __name__ == "__main__":
    main()
