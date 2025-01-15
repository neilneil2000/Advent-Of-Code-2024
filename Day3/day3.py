def main():
    data = open("Day3/day3_input.txt", "r").read()
    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print(part_1(data))
    print(part_2(data))


def part_1(data):
    total = 0
    while data:
        start = data.find("mul(")
        if start < 0:
            break
        data = data[start + 4 :]
        comma = data.find(",")
        if not 0 < comma <= 3:
            continue
        if not data[:comma].isdigit():
            continue
        operand_a = int(data[:comma])
        data = data[comma + 1 :]
        close = data.find(")")
        if not 0 < close <= 3:
            continue
        if not data[:close].isdigit():
            continue
        operand_b = int(data[:close])
        data = data[close + 1 :]
        total += operand_a * operand_b
    return total


def part_2(data):
    return sum(
        sum(map(part_1, x.split("do()")[1:])) for x in f"do(){data}".split("don't()")
    )


if __name__ == "__main__":
    main()
