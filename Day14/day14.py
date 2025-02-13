from day14_input import day14_example, day14_input


def movement(dimensions, steps):
    def mover(p, v):
        return (p[0] + steps * v[0]) % dimensions[0], (
            p[1] + steps * v[1]
        ) % dimensions[1]

    return mover


def process_inputs(inputs):
    processed = []
    for entry in inputs:
        p, v = entry.split()
        _, p = p.split("=")
        p = p.split(",")
        p = tuple(map(int, p))
        _, v = v.split("=")
        v = v.split(",")
        v = tuple(map(int, v))
        processed.append((p, v))
    return processed


def safety_factor(robots, dimensions):
    """Return multiple of number of robots in each quadrant"""
    a, b, c, d = 0, 0, 0, 0
    x_mid = dimensions[0] // 2
    y_mid = dimensions[1] // 2
    for x, y in robots:
        if x < x_mid and y < y_mid:
            a += 1
        elif x < x_mid and y > y_mid:
            b += 1
        elif x > x_mid and y < y_mid:
            c += 1
        elif x > x_mid and y > y_mid:
            d += 1
    return a * b * c * d


def main():
    dimensions = (101, 103)
    steps = 100

    robots = process_inputs(day14_input)
    mover = movement(dimensions, steps)
    positions = []
    for p, v in robots:
        positions.append(mover(p, v))
    ans = safety_factor(positions, dimensions)
    print(ans)


if __name__ == "__main__":
    main()
