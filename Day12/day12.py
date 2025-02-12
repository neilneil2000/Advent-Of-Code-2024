import operator
from day12_input import day12_example, day12_input, day12_cross


def main():
    my_garden = Garden(list(map(list, day12_input)))
    my_garden.populate_regions()
    print(f"Day 12 Part 1: {my_garden.fence_cost()}")
    print(f"Day 12 Part 2: {my_garden.discount_fence_cost()}")


class Fence:
    def __init__(self, a, b):
        self.adjacencies = {a, b}

    @property
    def direction(self):
        a, b = self.adjacencies
        if a[0] == b[0]:
            return "Horizontal"
        return "Vertical"


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

    def discount_cost(self):
        return self.area * self.count_sides()

    @staticmethod
    def adjacencies(location):
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        return {tuple(map(operator.add, location, d)) for d in directions}

    def get_fences(self, location):
        adj = self.adjacencies(location) - self.region
        ax, ay = location
        return {
            ((min(ax, bx), min(ay, by)), (max(ax, bx), max(ay, by))) for bx, by in adj
        }

    def get_all_fences(self):
        fences = set()
        for location in self.region:
            new_fences = self.get_fences(location)
            for a, b in new_fences:
                bx, by = b
                if a[0] == bx:
                    fences.add(((bx, by), (bx + 1, by)))
                else:
                    fences.add(((bx, by), (bx, by + 1)))
        return fences

    def count_sides(self):
        """Return number of sides in polygon(s) represented in a set"""
        fences = self.get_all_fences()
        sides = 0
        first = fences.pop()
        post_a, post_b = first
        previous = {(-5, -5), (-10, -10)}
        while fences:
            fences.discard((post_a, post_b))
            connected = {x for x in fences if post_a in x or post_b in x}
            for a, b in connected.copy():
                if a in previous or b in previous:
                    connected.remove((a, b))

            if len(connected) == 0:  # This polygon is complete - start next
                if self.is_corner(first, (post_a, post_b)):
                    sides += 1
                if fences:
                    previous = {post_a, post_b}
                    first = fences.pop()
                    post_a, post_b = first
                    continue
                break
            if len(connected) == 1:
                new = connected.pop()
                if self.is_corner(new, (post_a, post_b)):
                    sides += 1
                previous = {post_a, post_b}
                post_a, post_b = new
                continue
            for new in connected:
                if self.is_corner(new, (post_a, post_b)):
                    sides += 1
                    break
            previous = {post_a, post_b}
            post_a, post_b = new
        return sides

    def is_corner(self, fence_a, fence_b):
        """Returns two is fence_a and fence_b make a corner"""
        x = {fence_a[0][0], fence_a[1][0], fence_b[0][0], fence_b[1][0]}
        y = {fence_a[0][1], fence_a[1][1], fence_b[0][1], fence_b[1][1]}
        if len(x) == 1 or len(y) == 1:
            return False
        return True


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

    def discount_fence_cost(self):
        return sum(r.discount_cost() for r in self.regions)


if __name__ == "__main__":
    main()
