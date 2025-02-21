from collections import defaultdict

from day20_input import day20_input, day20_example


class Racer:
    def __init__(self, layout):
        self.layout = layout
        self.start = None
        self.end = None
        self.walls = set()
        self.track = set()
        self.costs = {}
        self._process_layout()
        self._calc_path_costs()
        self.cheats = defaultdict(set)

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

    def find_cheats(self):
        for wall in self.walls:
            if score := self.calc_cheat_scores_through_wall(wall):
                self.cheats[score].add(wall)

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


def main():
    racetrack = Racer(day20_input)
    racetrack.find_cheats()
    print(racetrack.cheats_over_x(100))


if __name__ == "__main__":
    main()
