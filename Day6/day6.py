from day6_input import main_map
from guard_map import GuardMap
import copy


def main():
    my_map = list(map(list, main_map))
    guard_map = GuardMap(my_map)
    guard_map.part_1()
    print(f"Day 6 Part 1: {guard_map.path_length()}")
    potential_obstacles = guard_map.path_values()
    total = 0
    for obstacle in potential_obstacles:
        new_map = list(map(list, main_map))
        x, y = obstacle
        new_map[y][x] = "#"
        validator = GuardMap(new_map)
        validator.part_1()
        if validator.in_bounds() and validator.is_loop():
            total += 1
    print(total)

    # my_map = list(map(list, main_map))
    # guard_map = GuardMap(my_map)
    # print(f"Day 6 Part 2: {guard_map.part_2()}")


if __name__ == "__main__":
    main()
