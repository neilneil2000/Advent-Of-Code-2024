import re


def main():
    data = open("Day3/day3_input.txt", "r").read()
    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print(f"Day 3 Part 1: {part_1(data)}")
    print(f"Day 3 Part 1: {part_2(data)}")


def part_1(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(int(x) * int(y) for x, y, in re.findall(pattern, data))


def part_2(data):
    return sum(
        sum(map(part_1, x.split("do()")[1:])) for x in f"do(){data}".split("don't()")
    )


if __name__ == "__main__":
    main()
