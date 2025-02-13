from day13_input import day13_input, day13_example


def solve_sim_equations(a, b, prize) -> tuple[float, float]:
    y = (a[0] * prize[1] - a[1] * prize[0]) / (a[0] * b[1] - a[1] * b[0])
    x = (prize[0] - b[0] * y) / a[0]
    return x, y


def process_file(input_string: str) -> list[tuple[int]]:
    entries = []
    for entry in input_string:
        new = []
        for line in entry.splitlines():
            _, line = line.split(":")
            a, b = line.split(",")
            a = a.replace("=", "+")
            b = b.replace("=", "+")
            _, a = a.split("+")
            _, b = b.split("+")
            new.append((int(a), int(b)))
        entries.append(tuple(new))
    return entries


def count_tokens(entries) -> int:
    total = 0
    for entry in entries:
        x, y = solve_sim_equations(*entry)
        if x.is_integer() and y.is_integer():
            total += int(3 * x + y)
    return total


def main():
    entries = process_file(day13_input)

    print(f"Day 13 Part 1: {count_tokens(entries)}")

    adj = 10000000000000
    entries = list((a[0], a[1], tuple(map(lambda x: x + adj, a[2]))) for a in entries)
    print(f"Day 13 Part 2: {count_tokens(entries)}")


if __name__ == "__main__":
    main()
