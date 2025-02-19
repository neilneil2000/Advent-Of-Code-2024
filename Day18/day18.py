from day18_input import day18_input

from collections import defaultdict
import math


class Memory:
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.best = None
        self.obstacles = set()

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
    print(my_memory.best[target_position])


if __name__ == "__main__":
    main()
