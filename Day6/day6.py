import operator

from day6_input import main_map


def main():
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    index = 0
    my_map = list(map(list, main_map))
    for y, row in enumerate(my_map):
        for x, cell in enumerate(row):
            if cell == "^":
                position = (x, y)
    try:
        while True:
            while my_map[position[1]][position[0]] != "#":
                my_map[position[1]][position[0]] = "X"
                position = tuple(map(operator.add, position, directions[index]))
            position = tuple(map(operator.sub, position, directions[index]))
            index = (index + 1) % 4
    except IndexError:
        print("Out of Bounds")

    print(sum(map(lambda x: x.count("X"), my_map)))


if __name__ == "__main__":
    main()
