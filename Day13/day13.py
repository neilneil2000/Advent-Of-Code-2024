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


def process_file(file_name):
    entries = []
    for entry in file_name:
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
    for entry in day13_example:
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
    print(len(entries))
    print(entries[0])
    print(*entries[0])
    print(sum(get_cost(*entry) for entry in entries))


if __name__ == "__main__":
    main()
