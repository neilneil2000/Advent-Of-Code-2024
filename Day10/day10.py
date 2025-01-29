import operator
from day10_input import day10_example, day10_input


def main():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    landscape = Topology(list(map(list, day10_input)), directions)
    total = 0
    for location in landscape.start_points():
        peaks = landscape.recursive_search(1, [location])
        # print(len(peaks), peaks)
        total += len(peaks)
    print(f"Day 10 Part 1: {total}")

    total = 0
    for location in landscape.start_points():
        peaks = landscape.recursive_chain_search(1, [[location]])
        print(location, len(peaks))
        total += len(peaks)
    print(f"Day 10 Part 2: {total}")


class Topology:
    def __init__(self, topology, valid_directions):
        self.topology = topology
        self.valid_directions = valid_directions
        self.start_point = "0"

    def start_points(self):
        locations = set()
        for y, row in enumerate(self.topology):
            for x, _ in enumerate(row):
                if self.topology[y][x] == self.start_point:
                    locations.add((x, y))
        return locations

    def get_potential_locations(self, start_locations, valid_directions):
        potential_locations = set()
        for location in start_locations:
            for direction in valid_directions:
                potential_locations.add(tuple(map(operator.add, location, direction)))
        return potential_locations

    def get_potential_chains(self, start_chains, valid_directions):
        potential_chains = []
        for chain in start_chains:
            for direction in valid_directions:
                new_location = tuple(map(operator.add, chain[-1], direction))
                potential_chains.append(chain + [new_location])
        return potential_chains

    def is_location_valid(self, location, number):
        x, y = location
        if (
            0 <= x < len(self.topology[1])
            and 0 <= y < len(self.topology)
            and self.topology[y][x] == str(number)
        ):
            return True
        return False

    def is_chain_valid(self, chain, number):
        return self.is_location_valid(chain[-1], number)

    def recursive_search(self, number, start_locations):
        potential_locations = self.get_potential_locations(
            start_locations, self.valid_directions
        )
        new_locations = {
            i for i in potential_locations if self.is_location_valid(i, number)
        }

        if number < 9:
            new_locations = self.recursive_search(number + 1, new_locations)
        return new_locations

    def recursive_chain_search(self, number, start_chains):
        potential_chains = self.get_potential_chains(
            start_chains, self.valid_directions
        )
        new_chains = [i for i in potential_chains if self.is_chain_valid(i, number)]

        if number < 9:
            new_chains = self.recursive_chain_search(number + 1, new_chains)
        return new_chains


if __name__ == "__main__":
    main()
