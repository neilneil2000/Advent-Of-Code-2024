DIGITPAD = {
    "0": (1, 0),
    "A": (2, 0),
    "1": (0, 1),
    "2": (1, 1),
    "3": (2, 1),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "7": (0, 3),
    "8": (1, 3),
    "9": (2, 3),
}

ARROWPAD = {"<": (0, 0), "^": (1, 1), "v": (1, 0), ">": (2, 0), "A": (2, 1)}

EXAMPLE = """029A
980A
179A
456A
379A""".splitlines()

INPUT = """083A
935A
964A
149A
789A"""


class Keypad:

    HOME_LOCATION = "A"
    RIGHT = ">"
    LEFT = "<"
    UP = "^"
    DOWN = "v"

    def __init__(self, keymap):
        self.keymap = keymap
        self.pointer = keymap[self.HOME_LOCATION]

    def move(self, end) -> list[str]:
        """Move pointer and return one list of moves that would work for this move"""
        if isinstance(end, str):
            end = self.keymap[end]
        right = end[0] - self.pointer[0]
        up = end[1] - self.pointer[1]

        moves = ""
        if right > 0:
            moves += self.RIGHT * right
        if up > 0:
            moves += self.UP * up
        if up < 0:
            moves += self.DOWN * -up
        if right < 0:
            moves += self.LEFT * -right

        self.pointer = end
        return moves


def mover(keypads: list[Keypad], buttons: list[str]):
    result = ""
    for button in buttons:
        if len(keypads) <= 1:
            result += keypads[0].move(button) + "A"
        else:
            result += mover(keypads[1:], keypads[0].move(button) + "A")
    return result


def main():
    keypads = [Keypad(DIGITPAD), Keypad(ARROWPAD), Keypad(ARROWPAD)]
    result = ""
    total = 0
    for line in EXAMPLE:
        result = mover(keypads, line)
        print(result)
        print(line, len(result), int(line[:-1]) * len(result))
        total += int(line[:-1]) * len(result)
    print(f"Day21 Part 1: {total}")


if __name__ == "__main__":
    main()
