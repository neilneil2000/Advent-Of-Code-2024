import operator


class GuardMap:
    def __init__(self, layout: list[list[str]]):
        self.__layout = layout
        self.__position = self.get_start()
        self.__directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.__arrows = ["^", ">", "v", "<"]
        self.__index = 0

    def get_start(self) -> tuple[int, int]:
        for y, row in enumerate(self.__layout):
            for x, cell in enumerate(row):
                if cell == "^":
                    return (x, y)

    def turn(self):
        self.__index = (self.__index + 1) % 4

    @property
    def direction(self) -> tuple[int, int]:
        return self.__directions[self.__index]

    def solve(self):
        try:
            while True:
                while self.__layout[self.__position[1]][self.__position[0]] != "#":
                    self.__layout[self.__position[1]][self.__position[0]] = "X"
                    self.__position = tuple(
                        map(operator.add, self.__position, self.direction)
                    )
                self.__position = tuple(
                    map(operator.sub, self.__position, self.direction)
                )
                self.turn()
        except IndexError:
            print("Out of Bounds")

    def path_length(self):
        return sum(map(lambda x: x.count("X"), self.__layout))
