import operator

from day16_input import day16_input, day16_example, day16_example2


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

    def depth_first(self, location, direction, score):
        if location[-1] == self.end:
            return score
        forward = self.forward(location[-1], direction[-1])
        scores = set()
        previous = list(zip(location, direction))
        if forward not in self.walls:
            scores &= self.depth_first(
                location + [forward],
                direction + [direction[-1]],
                score + self.FWD_SCORE,
            )

        if (location, left := self.left(direction)) not in previous:
            scores &= self.depth_first(
                location + [location[-1]],
                direction + [left],
                score + self.TURN_SCORE,
            )

        if (location, right := self.right(direction)) not in previous:
            scores &= self.depth_first(
                location + [location[-1]],
                direction + [right],
                score + self.TURN_SCORE,
            )
        return min(scores)

    def breadth_first(self, vectors: list, scores: list):
        new_vectors = []
        new_scores = []
        for vector, score in zip(vectors, scores):
            if vector[0] in self.walls or (
                vector in self.best and score >= self.best[vector]
            ):
                continue
            self.best[vector] = score
            location, direction = vector
            if location == self.end:
                continue
            new_vectors += [
                (self.forward(location, direction), direction),
                (location, self.left(direction)),
                (location, self.right(direction)),
            ]
            new_scores += [
                score + self.FWD_SCORE,
                score + self.TURN_SCORE,
                score + self.TURN_SCORE,
            ]
        if new_vectors:
            self.breadth_first(new_vectors, new_scores)

    def go_breadth(self):
        self.best = {}
        self.breadth_first([(self.start, self.initial_direction)], [0])

    def get_lowest_score(self):
        return min(
            self.best.get((self.end, d), 99999999999999999) for d in self.DIRECTIONS
        )


def main():
    reindeerMaze = Maze(day16_input, ">")
    reindeerMaze.go_breadth()
    ans = reindeerMaze.get_lowest_score()
    print(f"Day 16 Part 1: {ans}")


if __name__ == "__main__":
    main()
