from day18_input import day18_input

from collections import defaultdict
import math
import sys


class Memory:
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.best = None
        self.obstacles = set()
        self.flood = set()

    def initialise_best(self):
        self.best = defaultdict(lambda: math.inf)

    def load_obstacles(self, obstacles):
        self.obstacles |= set(obstacles)

    def breadth_first(self, frontier: set):
        new_frontier = set()
        for x, y in frontier:
            target_score = self.best[(x, y)] + 1
            possibles = {(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)}
            for new_x, new_y in possibles:
                if new_x < 0 or new_y < 0 or new_x > self.x_max or new_y > self.y_max:
                    continue
                if (new_x, new_y) in self.obstacles:
                    continue
                if self.best[(new_x, new_y)] <= target_score:
                    continue
                self.best[(new_x, new_y)] = target_score
                new_frontier.add((new_x, new_y))

        if new_frontier:
            self.breadth_first(new_frontier)

    def breadth_first_go(self, start_position):
        self.initialise_best()
        self.best[(0, 0)] = 0
        self.breadth_first({start_position})

    def flood_fill(self, x, y):
        self.flood.add((x, y))
        new_frontier = set()
        for new_x, new_y in {(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)}:
            if new_x < 0 or new_y < 0 or new_x > self.x_max or new_y > self.y_max:
                continue
            if (new_x, new_y) in self.obstacles:
                continue
            if (new_x, new_y) in self.flood:
                continue
            new_frontier.add((new_x, new_y))
        for x, y in new_frontier:
            self.flood_fill(x, y)

    def flood_fill_2(self, frontier):
        pass
        possibles = set()
        for x, y in frontier:
            if x < 0 or y < 0 or x > self.x_max or y > self.y_max:
                continue
            if (x, y) in self.obstacles:
                continue
            if (x, y) in self.flood:
                continue
            possibles.add((x, y))
        self.flood |= possibles
        new_frontier = {(x + 1, y) for x, y in possibles}
        new_frontier |= {(x - 1, y) for x, y in possibles}
        new_frontier |= {(x, y + 1) for x, y in possibles}
        new_frontier |= {(x, y - 1) for x, y in possibles}
        new_frontier -= frontier
        if new_frontier:
            self.flood_fill_2(new_frontier)

    def display(self):
        for y in range(self.y_max + 1):
            for x in range(self.x_max + 1):
                if (x, y) in self.obstacles:
                    print("#", end="")
                elif self.best[(x, y)] == math.inf:
                    print(".", end="")
                else:
                    print("O", end="")
            print()


def main():
    bytes = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in day18_input]

    x_max = 70
    y_max = 70
    number_of_bytes = 1024
    start_position = (0, 0)
    target_position = (70, 70)

    my_memory = Memory(x_max, y_max)
    my_memory.load_obstacles(bytes[:number_of_bytes])
    my_memory.breadth_first_go(start_position)
    ans = my_memory.best[target_position]
    my_memory.display()
    print(f"Day 18 Part 1: {ans}")

    final_byte = None
    for byte in bytes[number_of_bytes:]:
        my_memory.load_obstacles([byte])
        # my_memory.breadth_first_go(start_position)
        my_memory.flood = set()
        my_memory.flood_fill_2({start_position})

        if target_position not in my_memory.flood:
            final_byte = byte
            break
    # my_memory.display()
    print(f"Day 18 Part 2: {final_byte}")


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    main()
