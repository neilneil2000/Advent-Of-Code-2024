from day13_input import day13_input, day13_example


def find_values(prize, a, b):
    counter = 0
    x, y = prize
    ax, ay = a
    bx, by = b
    while x % ax or y % ay:
        counter += 1
        x -= bx
        if x < 0:
            return ()
        y -= by
        if y < 0:
            return ()
    if x // ax == y // ay:
        return (x // ax, counter)
    return ()


def get_cost(a, b, prize):
    solutions = set()
    new = find_values(prize, a, b)
    if new:
        solutions.add(new)
    new = find_values(prize, b, a)
    if new:
        solutions.add((new[1], new[0]))

    if solutions:
        return min(map(lambda x: 3 * x[0] + x[1], solutions))
    return 0


def solve_sim_equations(a, b, prize):
    x = zip(a, b, prize)
    # for entry in x:
    # print(entry)
    # b = (lk -in)/(im-lj)
    y = (a[0] * prize[1] - a[1] * prize[0]) / (a[0] * b[1] - a[1] * b[0])
    x = (prize[0] - b[0] * y) / a[0]
    return x, y


def are_parallel(x, y):
    """Return true if two lines are parallel"""
    return x[0] / x[1] == y[0] / y[1]


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


def main():
    entries = process_file(day13_input)
    # entries = [((94, 34), (22, 67), (8400, 5400))]
    print(sum(are_parallel(x[0], x[1]) for x in entries))
    total = 0
    for entry in entries:
        # print(are_parallel(entry[0], entry[1]))
        x, y = solve_sim_equations(*entry)
        if x.is_integer() and y.is_integer():
            print(f"Solution Found. x={x} y={y} Tokens = {3*x+y}")
            total += 3 * x + y
        # print(result)
    print(total)

    # print(sum(get_cost(*entry) for entry in entries))


if __name__ == "__main__":
    main()
