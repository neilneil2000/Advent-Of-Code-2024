from day1_input import DAY_1_INPUT


def process_data():
    list_a, list_b = zip(*map(lambda x: x.split(), DAY_1_INPUT.splitlines()))
    return list(map(int, list_a)), list(map(int, list_b))


def main():

    list_a, list_b = process_data()
    ans = sum(map(lambda x, y: abs(x - y), sorted(list_a), sorted(list_b)))
    print(f"Day 1 Part 1: {ans}")

    ans = sum(map(lambda x: list_b.count(x) * x, list_a))
    print(f"Day 1 Part 2: {ans}")


if __name__ == "__main__":
    main()
