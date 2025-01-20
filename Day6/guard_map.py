import operator


class GuardMap:
    def __init__(self, layout: list[list[str]], obstacle_step=None):
        self.__layout = layout
        self.obstacle_step = obstacle_step
        self.__start = self.get_start()
        self.__position = self.__start
        self.__directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.__arrows = ["^", ">", "v", "<"]
        self.__index = 0
        self.my_obstacles = set()
        self.__step_counter = 0
        self.path = [self.__position]

    def get_start(self) -> tuple[int, int]:
        """Locate starting position"""
        for y, row in enumerate(self.__layout):
            for x, cell in enumerate(row):
                if cell in ["^", {"^"}]:
                    self.__layout[y][x] = {"^"}
                    return (x, y)

    def turn(self):
        """Turn 90 degrees clockwise"""
        self.__index = (self.__index + 1) % 4

    @property
    def direction(self) -> tuple[int, int]:
        """Return tuple describing direction"""
        return self.__directions[self.__index]

    def part_1(self):
        """
        Execute Part 1 Solution
        """
        while True:
            self.forward()
            if not self.in_bounds() or self.is_loop():
                return
            if (
                self.obstacle_step is not None
                and self.obstacle_step == self.__step_counter
            ):
                if self.in_free_space():
                    self.place_obstacle()
                else:
                    self.__position = (-1, -1)
                    self.obstacle_step = None
                    return
            if self.is_obstacle():
                self.backward()
                self.turn()
            self.lay_trace()

    def path_values(self):
        path = set(self.path)
        path.remove(self.__start)
        return path

    def in_free_space(self):
        return self.__layout[self.__position[1]][self.__position[0]] == "."

    def place_obstacle(self):
        self.__layout[self.__position[1]][self.__position[0]] = "#"
        self.my_obstacles.add(self.__position)
        self.obstacle_step = None

    def is_loop(self):
        """True if loop detected"""
        return (
            self.__arrows[self.__index]
            in self.__layout[self.__position[1]][self.__position[0]]
        )

    def in_bounds(self):
        "True if __position is in bounds"
        x, y = self.__position
        return 0 <= x < len(self.__layout[1]) and 0 <= y < len(self.__layout)

    def lay_trace(self):
        """Mark current position as visited"""
        if isinstance(self.__layout[self.__position[1]][self.__position[0]], set):
            self.__layout[self.__position[1]][self.__position[0]].add(
                self.__arrows[self.__index]
            )
        else:
            self.__layout[self.__position[1]][self.__position[0]] = {
                self.__arrows[self.__index]
            }
        self.path.append(self.__position)

    def is_obstacle(self):
        """Return True if __position is obstacle"""
        return self.__layout[self.__position[1]][self.__position[0]] == "#"

    def path_length(self):
        """Return Number of locations in route"""
        total = 0
        for row in self.__layout:
            for cell in row:
                if isinstance(cell, set):
                    total += 1
        return total

    def forward(self):
        """Move Forward one position"""
        self.__position = tuple(map(operator.add, self.__position, self.direction))
        self.__step_counter += 1

    def backward(self):
        "Move backwards one position"
        self.__position = tuple(map(operator.sub, self.__position, self.direction))
        self.__step_counter -= 1
