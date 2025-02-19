from day17_input import register_a, register_b, register_c, prog


class Computer:
    def __init__(self, regs, program):
        self.reg_a, self.reg_b, self.reg_c = regs
        self.program = list(zip(program[::2], program[1::2]))
        self.ptr = 0
        self.target = program
        self.output = []

    def combo(self, arg):
        """Convert Combo Argument to Literal"""
        if arg < 4:
            return arg
        if arg == 4:
            return self.reg_a
        if arg == 5:
            return self.reg_b
        if arg == 6:
            return self.reg_c

        raise ValueError("Invalid arg")

    def run(self):
        """Execute Program"""
        while self.ptr < len(self.program):
            op, arg = self.program[self.ptr]
            if op == 0:
                self.reg_a >>= self.combo(arg)
            if op == 1:
                self.reg_b ^= arg
            if op == 2:
                self.reg_b = self.combo(arg) % 8
            if op == 3 and self.reg_a != 0:
                self.ptr = arg
                continue
            if op == 4:
                self.reg_b ^= self.reg_c
            if op == 5:
                self.output.append(self.combo(arg) % 8)
            if op == 6:
                self.reg_b = self.reg_a >> self.combo(arg)
            if op == 7:
                self.reg_c = self.reg_a >> self.combo(arg)
            self.ptr += 1

    def find_reg_a(self):
        """Find Lowest Entry of Register A that causes the program to print itself"""
        reg_a = 0
        solutions = [0]
        for target in self.target[::-1]:
            options = []
            for reg_a in solutions:
                reg_a <<= 3
                for i in range(8):
                    reg_b = i ^ 5 ^ 6 ^ ((reg_a + i) >> (i ^ 5))
                    if reg_b % 8 != target:
                        continue
                    options.append(reg_a + i)
            solutions = options
        return min(solutions)


def main():

    my_computer = Computer((register_a, register_b, register_c), prog)

    my_computer.run()
    print(f"Day 17 Part 1: {my_computer.output}")

    new_reg_a = my_computer.find_reg_a()
    print(f"Day 17 Part 2: {new_reg_a}")


if __name__ == "__main__":
    main()
