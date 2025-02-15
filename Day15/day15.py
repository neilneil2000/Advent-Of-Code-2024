from day15_input import day15_input, day15_example

import operator

VECTORS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


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


def parse_map_wide(layout):
    walls = set()
    boxes = set()
    robot = ()
    layout = layout.splitlines()
    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == "#":
                walls |= {(2 * x, y), (2 * x + 1, y)}
            elif cell == "@":
                robot = (2 * x, y)
            elif cell == "O":
                boxes.add(((2 * x, y), (2 * x + 1, y)))
    return walls, robot, boxes


def gps(boxes):
    return sum(x + 100 * y for x, y in boxes)


def gps_wide(boxes):
    return sum(min(x + 100 * y for x, y in box) for box in boxes)


def tuple_add(a, b):
    return tuple(map(operator.add, a, b))


def display(boxes, robot, walls, width, height):
    for y in range(height):
        for x in range(width):
            if (x, y) in walls:
                char = "#"
            elif (x, y) == robot:
                char = "@"
            elif type(list(boxes)[0][0]) == int:
                if (x, y) in boxes:
                    char = "O"
                else:
                    char = "."
            else:
                if any((x, y) == box[0] for box in boxes):
                    char = "["
                elif any((x, y) == box[1] for box in boxes):
                    char = "]"
                else:
                    char = "."
            print(char, end="")
        print()


def part_1(directions, walls, boxes: set, robot):
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
    return gps(boxes)


def ok_to_continue(boxes, pointers, walls):
    return not is_wall_within_pointers(pointers, walls) and get_boxes_within_pointers(
        pointers, boxes
    )


def increment_pointers(pointers, vector):
    return set(tuple_add(pointer, vector) for pointer in pointers)


def get_boxes_within_pointers(pointers, boxes):
    impacted_boxes = set()
    for pointer in pointers:
        for box in boxes:
            if pointer in box:
                impacted_boxes |= {box}
    return impacted_boxes


def is_wall_within_pointers(pointers, walls):
    return any(p in walls for p in pointers)


def part_2(directions, walls, boxes: set, robot: tuple):
    for direction in directions:
        # display(boxes, robot, walls, 20, 10)

        vector = VECTORS[direction]
        pointer = robot
        moving_boxes = set()

        if vector in ((-1, 0), (1, 0)):  # left/right
            pointer = tuple_add(pointer, vector)
            while any(pointer in x for x in boxes):
                if vector == (-1, 0):
                    new = (pointer, pointer := tuple_add(pointer, vector))
                    moving_boxes.add((new[1], new[0]))
                else:
                    moving_boxes.add((pointer, pointer := tuple_add(pointer, vector)))
                pointer = tuple_add(pointer, vector)
            if pointer in walls:
                continue

            robot = tuple_add(robot, vector)
            for left, right in moving_boxes:
                boxes.add((tuple_add(left, vector), tuple_add(right, vector)))
            boxes -= moving_boxes
        else:
            pointer = {tuple_add(pointer, vector)}
            while ok_to_continue(boxes, pointer, walls):
                new_boxes = get_boxes_within_pointers(pointer, boxes)
                moving_boxes |= new_boxes
                new_pointer = {location for box in new_boxes for location in box}
                pointer = increment_pointers(new_pointer, vector)
            if is_wall_within_pointers(pointer, walls):
                continue
            robot = tuple_add(robot, vector)
            boxes -= moving_boxes
            boxes |= {
                (tuple_add(l, vector), tuple_add(r, vector)) for l, r in moving_boxes
            }

    return gps_wide(boxes)


def main():

    layout, directions = day15_input

    walls, robot, boxes = parse_map(layout)
    print(f"Day 15 Part 1: {part_1(directions, walls, boxes, robot)}")

    walls, robot, boxes = parse_map_wide(layout)
    print(f"Day 15 Part 2: {part_2(directions, walls, boxes, robot)}")


if __name__ == "__main__":
    main()
