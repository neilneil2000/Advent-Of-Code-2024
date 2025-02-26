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

    def _get_neighbours(self, location: tuple[int, int]) -> set[tuple[int, int]]:
        """Return all neighbours of a given location"""
        x, y = location
        return {(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)}

    def find_simple_cheats(self):
        """Return all cheats that are a single step through a wall"""
        for wall in self.walls:
            if score := self.calc_cheat_scores_through_wall(wall):
                self.cheats[score].add(wall)

    def calc_cheat_scores_through_wall(self, wall: tuple[int, int]) -> int:
        """Return score of passing through wall"""
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

    def manhattan_distance(self, start: tuple[int, int], end: tuple[int, int]) -> int:
        """Return Manhattan distance between two x,y coordinates"""
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def get_long_cheats(self, min_cheat: int) -> dict:
        """Create Dictionary of All Cheats of at least length min_cheat"""
        all_cheats = {}
        for location in self.track:
            all_cheats |= self.find_cheats_from_here(location, min_cheat)
        return all_cheats

    def find_cheats_from_here(self, start: tuple[int, int], min_cheat: int) -> dict:
        """Build Dictionary of all cheats from start location that are of at least length min_cheat"""
        cheats = {}
        for location in self.track:
            dist = self.manhattan_distance(start, location)
            if dist > min_cheat:
                continue
            benefit = (self.costs[(location)] - self.costs[(start)]) - dist
            if benefit > 0:
                cheats[(start, location)] = benefit
        return cheats

    def summarise_cheats(self, cheats: dict) -> dict:
        """Create Summary of cheat dictionary"""
        summary = defaultdict(int)
        for v in cheats.values():
            summary[v] += 1
        return summary

    def count_cheats_over(self, cheat_summary: dict, cheat_target: int) -> int:
        """Return number of cheats over a certain value"""
        return sum(value for key, value in cheat_summary.items() if key >= cheat_target)


def main():
    racetrack = Racer(day20_input)
    cheat_target = 100
    racetrack.find_simple_cheats()
    print(f"Day 20 Part 1: {racetrack.cheats_over_x(cheat_target)}")

    cheat_length = 20
    cheats = racetrack.get_long_cheats(cheat_length)
    summary = racetrack.summarise_cheats(cheats)
    ans = racetrack.count_cheats_over(summary, cheat_target)
    print(f"Day 20 Part 2: {ans}")


if __name__ == "__main__":
    main()
