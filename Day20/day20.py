import math
from collections import defaultdict

from day20_input import day20_input, day20_example


class Racer:
    def __init__(self, layout):
        self.layout = layout
        self.start = None
        self.end = None
        self.walls = set()
        self.track = set()
        self.costs = defaultdict(int)
        self._process_layout()
        self._calc_path_costs()
        self.cheats = defaultdict(set)
        self.long_cheats = defaultdict(int)

    def _process_layout(self):
        for y, row in enumerate(self.layout):
            for x, char in enumerate(row):
                if char == "#":
                    self.walls.add((x, y))
                    continue
                if char == "S":
                    self.start = (x, y)
                elif char == "E":
                    self.end = (x, y)
                self.track.add((x, y))

    def _calc_path_costs(self):
        score = 0
        track = self.track.copy()
        location = self.start
        while True:
            self.costs[location] = score
            score += 1
            track.remove(location)
            if location == self.end:
                break
            location = self._get_neighbours(location) & track
            if len(location) > 1:
                raise ValueError("Too many neighbours")
            location = location.pop()

    def _get_neighbours(self, location):
        x, y = location
        return {(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)}

    def find_simple_cheats(self):
        for wall in self.walls:
            if score := self.calc_cheat_scores_through_wall(wall):
                self.cheats[score].add(wall)

    def find_long_cheats(self, cheat_length):
        solutions = set()
        for track in list(self.costs.keys()):
            result = self.breadth_first(track, cheat_length)
            for key in result.keys():
                saving = abs(self.costs[track] - self.costs[key]) - 2
                if saving > 0:
                    self.long_cheats[saving] += 1
        pass
        return sum(x for x in self.long_cheats)

    def depth_first(self, path, max_depth) -> set:
        solutions = set()
        # self.display(path)
        if len(path) > max_depth:
            return solutions
        here = path[-1]
        for neighbour in self._get_neighbours(here):
            if neighbour in path:
                continue
            if neighbour in self.track:
                solutions.add((path[0], neighbour))
                continue
            if neighbour in self.walls:
                solutions |= self.depth_first(path + [neighbour], max_depth)
        return solutions

    def breadth_first(
        self,
        frontier,
        max_score,
        scores=None,
        current_score=0,
    ):
        if scores is None:
            scores = defaultdict(lambda: math.inf)
        if not isinstance(frontier, set):
            frontier = {frontier}
        # self.display(scores, frontier)
        new_frontier = set()
        for location in frontier:
            if current_score < scores[location]:
                scores[location] = current_score
                if location in self.track and current_score > 0:
                    continue
                new_frontier |= self._get_neighbours(location)
                scores[location] = current_score
        new_frontier -= frontier
        new_frontier -= self.track
        new_frontier.discard(self.start)
        new_frontier.discard(self.end)
        if current_score < max_score:
            scores |= self.breadth_first(
                new_frontier, max_score, scores, current_score + 1
            )
        return scores

    def calc_cheat_scores_through_wall(self, wall):
        track = list(self._get_neighbours(wall) & self.track)
        if len(track) > 3:
            raise ValueError(f"Found Wall with too many track elements: {wall}")
        if len(track) == 3:
            a, b, c = track
            if a[0] == b[0] or a[1] == b[1]:
                track.pop(2)
            elif a[0] == c[0] or a[1] == c[1]:
                track.pop(1)
            else:
                track.pop(0)
        if len(track) < 2:
            return 0
        return abs(self.costs[track[0]] - self.costs[track[1]]) - 2

    def cheats_over_x(self, x):
        """Return number of cheats >=x"""
        return sum(len(values) for key, values in self.cheats.items() if key >= x)

    def display(self, scores, frontier):
        for y in range(15):
            for x in range(15):
                char = "."
                if (x, y) in scores:
                    char = scores[(x, y)]
                elif (x, y) in frontier:
                    char = "?"
                elif (x, y) in self.walls:
                    char = "#"
                elif (x, y) == self.start:
                    char = "S"
                elif (x, y) == self.end:
                    char = "E"
                print(char, end="")
            print()
        print()


def main():
    racetrack = Racer(day20_example)
    racetrack.find_simple_cheats()
    print(f"Day 20 Part 1: {racetrack.cheats_over_x(100)}")

    cheat_length = 20
    ans = racetrack.find_long_cheats(cheat_length)
    print(f"Day 20 Part 2: {ans}")


if __name__ == "__main__":
    main()
