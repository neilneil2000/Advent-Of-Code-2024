from day14_input import day14_example, day14_input


def movement(dimensions, steps):
    """Return function which moves a number of steps"""

    def mover(p, v):
        return (p[0] + steps * v[0]) % dimensions[0], (
            p[1] + steps * v[1]
        ) % dimensions[1]

    return mover


def process_inputs(inputs):
    """Process Input Text"""
    processed = []
    for entry in inputs:
        p, v = entry.split()
        p = p.split("=")[1].split(",")
        v = v.split("=")[1].split(",")
        processed.append((tuple(map(int, p)), tuple(map(int, v))))
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

    ans = safety_factor((mover(*robot) for robot in robots), dimensions)
    print(f"Day 14 Part 1: {ans}")


if __name__ == "__main__":
    main()
