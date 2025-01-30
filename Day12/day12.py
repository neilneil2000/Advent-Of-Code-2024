import operator
from day12_input import day12_example, day12_input


def main():
    my_garden = Garden(list(map(list, day12_input)))
    my_garden.populate_regions()
    print(f"Day 12 Part 1: {my_garden.fence_cost()}")


class Region:
    def __init__(self, region):
        self.region = region

    @property
    def area(self):
        """Return area of region"""
        return len(self.region)

    @property
    def perimeter(self):
        """Return perimeter of region"""
        total = 0
        for location in self.region:
            total += 4 - len(self.adjacencies(location) & self.region)
        return total

    @property
    def fence_cost(self):
        return self.area * self.perimeter

    @staticmethod
    def adjacencies(location):
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        return {tuple(map(operator.add, location, d)) for d in directions}


class Garden:
    def __init__(self, layout):
        self.layout = layout
        self.regions: list[Region] = []

    def populate_regions(self):
        for y, row in enumerate(self.layout):
            for x, symbol in enumerate(row):
                if symbol == ".":
                    continue
                self.add_region((x, y))

    def add_region(self, location):
        self.regions.append(Region(self.flood_fill(location)))

    def flood_fill(self, location):
        """Update topology by flood filling from location with identical values and return region"""
        x, y = location
        symbol, self.layout[y][x] = self.layout[y][x], "."

        new_locations = {location}
        for adj in Region.adjacencies(location):
            if not self.is_within_layout(adj):
                continue
            x, y = adj
            if not self.layout[y][x] == symbol:
                continue
            new_locations |= self.flood_fill(adj)

        return new_locations

    def is_within_layout(self, location):
        x, y = location
        return 0 <= x < len(self.layout[0]) and 0 <= y < len(self.layout)

    def fence_cost(self):
        return sum(r.fence_cost for r in self.regions)


if __name__ == "__main__":
    main()
