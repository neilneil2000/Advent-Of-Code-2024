def main():
    data = open("Day3/day3_input.txt", "r").read()
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
    print(total)


if __name__ == "__main__":
    main()
