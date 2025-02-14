from day15_input import day15_input, day15_example

import operator


def parse_map(layout):
    walls = set()
    boxes = set()
    robot = ()
    layout = layout.splitlines()
    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "@":
                robot = (x, y)
            elif cell == "O":
                boxes.add((x, y))
    return walls, robot, boxes


def gps(boxes):
    return sum(x + 100 * y for x, y in boxes)


def tuple_add(a, b):
    return tuple(map(operator.add, a, b))


def main():
    VECTORS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    layout, directions = day15_input
    walls, robot, boxes = parse_map(layout)

    for direction in directions:
        vector = VECTORS[direction]
        pointer = robot

        pointer = tuple_add(pointer, vector)
        while pointer in boxes:
            pointer = tuple_add(pointer, vector)
        if pointer in walls:
            continue

        robot = tuple_add(robot, vector)
        boxes.add(pointer)
        boxes.remove(robot)
    print(gps(boxes))


if __name__ == "__main__":
    main()
