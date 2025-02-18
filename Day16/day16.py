import operator
import math

from day16_input import day16_input, day16_example, day16_example2

from Tree import Tree

from collections import defaultdict, namedtuple
from dataclasses import dataclass, field


@dataclass
class NeilNode:
    score: int = math.inf
    children: set = field(default_factory=set)
    parents: set = field(default_factory=set)


class Maze:

    VECTORS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    DIRECTIONS = ["^", ">", "v", "<"]
    FWD_SCORE = 1
    TURN_SCORE = 1000

    def __init__(self, layout, initial_direction):
        self.layout = layout
        self.initial_direction = initial_direction
        self.start = None
        self.end = None
        self.walls = set()
        self.process_layout()
        self.best = {}
        self.paths = {}
        self.tree = defaultdict(lambda: NeilNode())

    def process_layout(self):
        for y, row in enumerate(self.layout):
            for x, char in enumerate(row):
                if char == "#":
                    self.walls.add((x, y))
                elif char == "S":
                    self.start = (x, y)
                elif char == "E":
                    self.end = (x, y)

    @classmethod
    def forward(cls, location: tuple[int, int], direction: str):
        return tuple(map(operator.add, location, cls.VECTORS[direction]))

    @classmethod
    def left(cls, direction):
        return cls.DIRECTIONS[(cls.DIRECTIONS.index(direction) - 1) % 4]

    @classmethod
    def right(cls, direction):
        return cls.DIRECTIONS[(cls.DIRECTIONS.index(direction) + 1) % 4]

    def breadth_first_paths(self, currents: list, paths: list, scores: list):
        new_paths = []
        new_scores = []
        new_currents = []
        for current, path, score in zip(currents, paths, scores):
            location, direction = current
            if location in self.walls:
                continue
            if current in self.best:
                if score > self.best[current]:
                    continue
                elif score == self.best[current]:
                    self.paths[current] |= path

            self.paths[current] = {location} | path
            self.best[current] = score
            if location == self.end:
                continue
            if score >= self.get_lowest_score():
                continue

            new_currents += [
                (self.forward(location, direction), direction),
                (location, self.left(direction)),
                (location, self.right(direction)),
            ]
            new_paths += [self.paths[current], self.paths[current], self.paths[current]]
            new_scores += [
                score + self.FWD_SCORE,
                score + self.TURN_SCORE,
                score + self.TURN_SCORE,
            ]
        if new_currents:
            self.breadth_first_paths(new_currents, new_paths, new_scores)

    def breadth_first_paths_2(self, vectors: list):
        next_vectors = []
        for l, d in vectors:
            score = self.tree[(l, d)].score
            possibles = {
                (self.forward(l, d), d, score + self.FWD_SCORE),
                (l, self.left(d), score + self.TURN_SCORE),
                (l, self.right(d), score + self.TURN_SCORE),
            }
            for new_l, new_d, new_score in possibles:
                if new_l in self.walls:
                    continue
                if (new_l, new_d) in self.tree[(l, d)].parents:
                    continue
                current_score = self.tree[(new_l, new_d)].score
                if new_score > current_score:
                    continue
                if new_score < current_score:
                    score_diff = current_score - new_score
                    self.tree[(new_l, new_d)].score = new_score
                    for child in self.tree[(new_l, new_d)].children:
                        self.subtract_to_leaf(child, score_diff)
                self.tree[(new_l, new_d)].parents.add((l, d))
                self.tree[(l, d)].children.add((new_l, new_d))
                if self.end == (new_l, new_d):
                    continue
                next_vectors.append((new_l, new_d))

        if next_vectors:
            self.breadth_first_paths_2(next_vectors)

    def subtract_to_leaf(self, start_node: NeilNode, subtraction: int):
        if not self.tree[start_node].children:
            self.tree[start_node].score -= subtraction
            return
        for child in self.tree[start_node].children:
            self.subtract_to_leaf(child, subtraction)

    def go_breadth(self):
        self.best = {}
        self.breadth_first_paths(
            [(self.start, self.initial_direction)], [{self.start}], [0]
        )

    def go_breadth_2(self):
        self.tree[(self.start, self.initial_direction)] = NeilNode(score=0)
        self.breadth_first_paths_2([(self.start, self.initial_direction)])

    def get_lowest_score(self):
        return min(self.tree[(self.end, d)].score for d in self.DIRECTIONS)
        # return self.best[self.end]

    def get_number_of_seats(self):
        # There could be more than one direction on final node
        nodes = [self.tree[(self.end, d)] for d in self.DIRECTIONS]
        lowest_score = self.get_lowest_score()
        for node in nodes.copy():
            if node.score != lowest_score:
                nodes.remove(node)
        all_nodes = {self.end}
        for node in nodes:
            all_nodes |= self.get_parent_locations(node)
            print(all_nodes)
        return len(all_nodes)

    def get_parent_locations(self, node):
        parents = set()
        for parent in node.parents:
            parents |= {parent[0]}
            parents |= self.get_parent_locations(self.tree[parent])
        return parents


def main():
    reindeer_maze = Maze(day16_example, ">")
    reindeer_maze.go_breadth_2()
    print(f"Day 16 Part 1: {reindeer_maze.get_lowest_score()}")
    print(f"Day 16 Part 2: {reindeer_maze.get_number_of_seats()}")


if __name__ == "__main__":
    print("Day 16")
    main()
