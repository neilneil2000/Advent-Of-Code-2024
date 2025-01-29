def main():
    stone_list = "572556 22 0 528 4679021 1 10725 2790".split()
    stone_list = list(map(int, stone_list))
    my_stones = Stones(stone_list)
    print(my_stones.stones)
    for i in range(25):
        my_stones.blink()
        print(f"{i + 1}:{len(my_stones.stones)}")


class Stones:
    def __init__(self, stones):
        self.stones = stones

    def process_stone(self, stone: int) -> list[int]:
        if stone == 0:
            return [1]
        if len(str(stone)) % 2 == 0:
            stone = str(stone)
            return [int(stone[: len(stone) // 2]), int(stone[len(stone) // 2 :])]
        return [stone * 2024]

    def blink(self):
        new_stones = []
        for stone in self.stones:
            new_stones.extend(self.process_stone(stone))
        self.stones = new_stones


if __name__ == "__main__":
    main()
