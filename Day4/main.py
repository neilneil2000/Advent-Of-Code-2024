from day4_input import big_words


def count_words(words, check_word="XMAS"):
    """Number of check_word in words"""
    words = ["".join(word) for word in words]
    return sum(map(lambda x: x.count(check_word) + x[::-1].count(check_word), words))


def part_1(rows):
    """Solve wordsearch returning total number of instances of XMAS"""
    l = len(rows) - 1
    slash = zip(*["." * (l - i) + row + "." * i for i, row in enumerate(rows)])
    backslash = zip(*["." * i + row + "." * (l - i) for i, row in enumerate(rows)])
    columns = list(zip(*rows))

    return (
        count_words(rows)
        + count_words(slash)
        + count_words(backslash)
        + count_words(columns)
    )


def is_xmas(loc, data):
    """True if locations forms Cross of XMAS"""
    x, y = loc
    try:
        return (
            {"M", "S"}
            == {data[y - 1][x - 1], data[y + 1][x + 1]}
            == {data[y - 1][x + 1], data[y + 1][x - 1]}
        )
    except IndexError:
        return False


def part_2(data):
    """Count number of XMAS crosses"""
    total = 0
    for j, row in enumerate(data):
        for i, letter in enumerate(row):
            if letter == "A" and is_xmas((i, j), data):
                total += 1
    return total


def main():
    data = big_words.splitlines()

    print(f"Day 4 Part 1: {part_1(data)}")
    print(f"Day 4 Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
