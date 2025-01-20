import itertools
from day8_input import day8_input


def main():
    city = [list(x) for x in day8_input]
    antennae = build_antenna_dictionary(city)
    antinodes = calculate_antinodes(antennae)
    remove_out_of_bounds(antinodes, x_max=len(city[0]) - 1, y_max=len(city) - 1)
    print(len(antinodes))
    antinodes = calculate_antinodes_2(
        antennae, x_max=len(city[0]) - 1, y_max=len(city) - 1
    )
    print(antinodes)
    print(len(antinodes))


def build_antenna_dictionary(city):
    antennae = {}
    for y, row in enumerate(city):
        for x, freq in enumerate(row):
            if freq == ".":
                continue
            antennae[freq] = {(x, y)}.union(antennae.get(freq, set()))
    return antennae


def calculate_antinodes(antennae):
    """Generate list of antinodes for antennae"""
    antinodes = set()
    for _, nodes in antennae.items():
        for a, b in itertools.combinations(nodes, 2):
            antinodes |= calculate_antinode_pair(a, b)
    return antinodes


def calculate_antinodes_2(antennae, x_max, y_max):
    """Generate list of antinodes for antennae"""
    antinodes = set()
    for _, nodes in antennae.items():
        for a, b in itertools.combinations(nodes, 2):
            antinodes |= calculate_all_antinodes_in_bounds(a, b, x_max, y_max)
    return antinodes


def remove_out_of_bounds(locations, x_max, y_max):
    for location in locations.copy():
        x, y = location
        if 0 <= x <= x_max and 0 <= y <= y_max:
            continue
        locations.remove(location)


def in_bounds(location, x_max, y_max):
    x, y = location
    return 0 <= x <= x_max and 0 <= y <= y_max


def calculate_antinode_pair(a, b):
    """Return antinode locations for two antennae at a,b"""
    ax, ay = a
    bx, by = b
    return {(2 * ax - bx, 2 * ay - by), (2 * bx - ax, 2 * by - ay)}


def calculate_all_antinodes_in_bounds(a, b, x_max, y_max):
    ax, ay = a
    bx, by = b

    x_diff = bx - ax
    y_diff = by - ay

    antinodes = {a, b}
    n = 1
    while True:
        new = (ax - (n * x_diff), ay - (n * y_diff))
        if not in_bounds(new, x_max, y_max):
            break
        antinodes.add(new)
        n += 1
    n = 1
    while True:
        new = (bx + (n * x_diff), by + (n * y_diff))
        if not in_bounds(new, x_max, y_max):
            break
        antinodes.add(new)
        n += 1
    return antinodes


if __name__ == "__main__":
    main()
