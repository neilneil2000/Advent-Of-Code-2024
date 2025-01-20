from day7_input import day7


def main():
    total = 0
    for equation in day7:
        target, operands = equation.split(":")
        target = int(target)
        operands = list(map(int, operands.split()))
        if is_valid(target, operands):
            total += target
    print(total)


def is_valid(target, operands):
    if len(operands) > 2:
        return (
            is_valid(target, [operands[0] + operands[1]] + operands[2:])
            or is_valid(target, [operands[0] * operands[1]] + operands[2:])
            or is_valid(
                target, [int(str(operands[0]) + str(operands[1]))] + operands[2:]
            )
        )
    return target in [
        operands[0] + operands[1],
        operands[0] * operands[1],
        int(str(operands[0]) + str(operands[1])),
    ]


if __name__ == "__main__":
    main()
