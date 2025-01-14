from day1_input import DAY_1_INPUT


def process_data():
    list_a, list_b = zip(*map(lambda x: x.split(), DAY_1_INPUT.splitlines()))
    return map(int, list_a), map(int, list_b)


def main():

    list_a, list_b = process_data()
    ans = sum(map(lambda x, y: abs(x - y), sorted(list_a), sorted(list_b)))
    print(f"Day 1 Part 1: {ans}")


if __name__ == "__main__":
    main()
