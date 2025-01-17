from day6_input import main_map
from guard_map import GuardMap


def main():
    my_map = list(map(list, main_map))
    guard_map = GuardMap(my_map)
    guard_map.solve()
    print(f"Day 6 Part 1: {guard_map.path_length()}")


if __name__ == "__main__":
    main()
