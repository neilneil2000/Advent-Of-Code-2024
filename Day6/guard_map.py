class GuardMap:
    def __init__(self, layout: list[str]):
        self.__layout = layout
        self.__position = self.get_start()
        self.__directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
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

    def move(self):
        while self.__position != "#":
            x, y = self.__position
            self.__layout[y][x] = "X"
    
    def get_
