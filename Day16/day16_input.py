day16_example = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()

day16_example2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()

day16_input = """#############################################################################################################################################
#.#.........#.#...#...#...........#.....#.......#...#...........#.............#.....#.......#.......................................#......E#
#.#.#.#####.#.#.#.#.#.#.#######.#.#.###.###.#.###.#.#.###.#######.#######.###.#.###.#.###.#.#######.###.#.#.#.#.#.#.###.###########.#####.#.#
#.#.#.....#...#.#...#.......#...#...#.......#.................#.....#.....#.#...#...#.#...#.#.......#...#.#...#...#.#...#...#...#.........#.#
#.#.#####.#####.#.###.#####.#.#####.###.#######.#####.###.###.#.#####.#####.#####.#####.###.#.#######.###.#.#######.#.#.#.#.#.#.#.###########
#.#.#...#...#...#.....#...#.#.........#.#.......#.#.....#.#...#.#.....#...........#.....#.....#...#.......#...#.#.....#.#.#.#.#.#...#.......#
#.#.###.###.#.###.#.#.#.#.#####.###.#.#.#.#######.#.#.#.###.###.#.#####.#############.#.#######.###.#.#.###.#.#.#.#####.#.#.#.#.#####.#####.#
#.#...#...#.#.#...#.#...#.#...#.....#.#.#...#.....#.#.......#...#.#...#...#.........#.....#.#.........................#.#.#...#...#...#.....#
#.###.#.#.#.#.###.#.#.###.#.#.#.###.#.#.###.#.###.#.#.#####.#.###.#.#.###.#######.#.#.#.#.#.#.#.#.###.#.#.#.#.#####.#.#.#.#######.#.###.#####
#.#...#.#.#.......#.#.#...#.#.#.#.....#.#.#...#.#.#.....#...#.#.#.......................#.#.............#...#...#...#.#.#.......#.#.#...#...#
#.#.###.#########.#.#.###.#.#.#.#.#.###.#.#####.#.###.#.#.#.#.#.#.#.#######.#.#####.###.#.#.#######.#.#.#.#####.#.###.#########.#.#.#.#.#.#.#
#...#...#.....#.#.#.#...#...#...#.....#.#.......#...#.#.#...#...#.#.#.....#...#...#.......#.#.......#...#.#...#...#.#.....#.....#...#.#.#.#.#
#.#####.#.###.#.#.#.#.#.#####.#####.#.#.#.#####.###.#.#.#.#.###.#.#.#.#.#.#####.#######.###.#.#.#########.#.#.#####.###.#.#.#####.#.#.###.#.#
#.......#.#.#.#...#...#...#.#.........#...#.......#...#.........#.#...#.#.#.........#.......#...#.....#...#.#.......#...#...#...#...#.....#.#
#.#.#####.#.#.#.#.#.#.###.#.###############.#####.###.###.#.#####.#####.#.#.#######.#.#.#####.#.#.#.###.###.#.###.###.#.#####.#.###.#######.#
#...#.....#.#.#.....#.....#.....#...........#...#...#.......#...#.#.....#.#.....#...#.#.....#.#...#...#...#.#.#.......#.#...#.#...#.......#.#
#.###.#####.#.###.###.#.#######.#.###.#.#####.#.###.#####.#.#.#.#.#.#####.#####.#.#.#.###.#.#.#######.###.#.#.#.#######.#.#.#.###.#.###.#.#.#
#...#.#.#...#...#.#...#.#.....#...#...#...#...#.........#.#...#.#.#.#...#.#.#...#.#.#...#.#.#.#.....#.....#.#.#.#.....#...#...#...#.#...#...#
#.#.#.#.#.#.###.#.#.#####.###.#.###.#####.###.#.#########.#.###.#.#.#.#.#.#.#.###.#####.#.###.###.#.#######.#.#.#.#.###########.###.#.#####.#
#...#.#.#.#...#.#.#.........#.#.#.#...........#.#.....#...#.#.#...#.#.#...#...#...#...#.#.#...#...#.....#...#.#.#.............#.......#.#...#
#.###.#.#.#.###.#########.###.#.#.###############.###.#.###.#.#####.#.#########.###.#.#.#.#.###.#########.###.#.#.###.###########.#.###.#.###
#...#.#...#.............#.#...#.......#.......#...#.#.#...#.#.......#...#.......#...#...#.#.#...............#.#.#...#...#...........#.......#
#####.#.###############.###.#########.#.#####.#.###.#.###.#.#.###.#####.#.#######.#######.#.###.#########.###.#.###.###.#.#######.#.#.#######
#.....#.#.#...#.......#.#...#.......#.#.#...#.#.#...#...#.#.#...#...#.#...#.......#.......#...#.#...#...#.#...#...#...#.#.......#.#.....#...#
#.###.#.#.#.#.#.#####.#.#.###.#.#####.#.#.#.#.#.#.#.#.###.#.###.###.#.###.#.#######.#.###.###.###.#.#.#.###.#.###.#####.#######.#.#.#####.#.#
#.#.....#.#.#...#.#...#...#...#.......#.#.#.#...#.#.#.....#.#...#...#.....#.#.......#.#.....#.#...#.........#...#...#.....................#.#
#.###.###.#.#####.#.#######.#####.#####.#.#.#####.#.#######.#####.###.#####.#.#.#.###.#.#####.#.#####.#############.#.#######.#####.#.#.#.#.#
#...#.#...#.#...#.#.#.......#.........#...#.......#.#.#.....#.....#.....#...#.#.....#.#.......#.#.....#.....#.......#.#.......#.....#.#...#.#
###.#.#.#.#.#.#.#.#.#####.###.###.#################.#.#.#.###.#.#########.###.#######.#.#######.#######.###.#.#.#.###.#.#######.###.#.#####.#
#.................#.....#...#.#...#...............#...#.#...#.............#.....#...#.#.......#.......#...#.#.#...#...#...#...#...#...#...#.#
#.###.#####.#.###.#####.###.#.#.###.#.#.#######.#####.#.#.#.#########.###########.#.#.#######.#.#.###.###.#.#.#.###.#.###.#.#.###.#####.#.#.#
#.#...#...#...#.......#...#...#.#...#.#.#.....#.#.....#...#.........#.........#...#.#.......#.#.#...#.....#...#.....#...#...............#.#.#
#.#.#.#.#.#.###########.#.#####.#.###.###.###.#.#.#################.#.#######.#.###.#.#######.#.###.###########.#######.#####.#.###.#######.#
#...#...#...#...#.......#.#.....#...........#.#.#.#.........#...#...#.#...#...#.#...#.....#...#...#...#...#.......#.....#.#...#.#...#...#...#
#.###.#######.#.#.#######.#.#######.#########.#.#.#####.###.#.#.#.#####.#.#.###.#.#######.#.#####.###.#.#.#.#####.###.###.#.###.#.###.#.#.#.#
#.......................#...#.....#.....#.....#.#.......#.....#.#.....#.#.#.....#.#.......#...#...#...#.#.#.....#...#.....#.....#...#.#...#.#
#####.#######.#.###.###.#.###.#.#######.#.#######.#######.#####.#####.#.#.#######.#.#.#######.#.#.#.###.#.#####.###.#######.#######.#.#####.#
#...#.#.......#...#.#.#.#.#...#.....#...#.#.........#.........#.#...#...#...#.#...#.........#...#.#.....#...#.......#.......#...#...#.#...#.#
#.###.#.#########.#.#.#.#.#.#######.#.###.#.###.#####.###.#.###.#.#.#######.#.#.###.#####.###.#############.#.#####.#.#######.#.#.###.#.###.#
#.#...#.#.......#.....#.#.#.#...#.#...#...#...#.....#...#.#.#...#.#.#.#...#.#.#...#.#...#.....#...........#.#.....#.#.....#...#...#...#.#...#
#.#.#.#.###.#####.#####.#.#.#.#.#.#####.#####.#####.###.#.###.###.#.#.#.#.#.#.###.#.###.###.###.#########.#.###.#.#######.#.#######.#.#.#.###
#.#...#...#...#...#.....#.#...#.#.#...#.....#.#.....#...#.....#.......#.#...#.....#.........#.#.#...#.....#...#.#.........#.#.......#.#.#...#
#.#.#.###.#.#.#.###.#####.#####.#.#.#.###.###.#.#####.#########.#####.#.#####.#############.#.#.###.#.#.#.###.#########.#.#.###.#.###.#.###.#
#...#...#.#.#...#...#...#.......#...#.#...#...#.#.....#.......#...#...#...#...#.......#.....#.#...#...#.....#.......#...#.#...#.#.#...#.....#
#.###.#.#.#.#####.###.#.#####.###.###.#.###.###.#.#####.###.###.#.#######.#.###.#.#####.#####.###.#.#######.###.###.#.#.#####.#.#.#.###.#####
#.#...#...#...#.#.....#.#...#...#...#.#.....#.#.#.#.....#.#.#...#.....#...#.....#...........#.#...#...#...#...#...#...#.#.............#...#.#
#.#.#########.#.#.#####.#.#.###.#####.#######.#.#.#.###.#.#.#.#######.#.#######.###.#.#####.#.#.#####.#.#.###.#########.#.#.#.#.#.###.###.#.#
#.#...#.....#.#...#...#.#.#...#.#...#.............#...#...#...#.#...#.#.#.....#...........#...#.#.....#.#...#.........#.#.#.....#...#...#...#
#.###.#.###.#.#.###.#.#.#.#.#.#.#.#.###.#####.#####.#.###.#####.#.#.#.#.#.###.###########.###.#.###.###.#.#.#########.#.#.#####.###.###.###.#
#.#...#...#...#...#.#...#.#.#.#...#...#.#.....#.....#...#...#...#.#...#...#.#.#.......#...#...#.#.......#.#...#.....#...#.#.....#.....#.#...#
#.#.#####.#########.#####.#.#########.###.###.#####.###.###.#.###.#.###.#.#.#.#.###.###.#######.#.#######.#.###.#.#####.#.#.#####.###.#.###.#
#.#.....#...#.............#.#...#.....#...#.#.#.....#.#.#...#.#...#.#...#...#.....#.....#...#...#...#.....#.#...#...#...#.#...#...#.#.#...#.#
#.#####.###.###.#####.#####.#.#.#.#####.###.#.#.#####.#.#.###.#.#####.#############.#.###.#.#.#.###.#.#####.#.#####.#.#.#.#####.###.#.###.#.#
#.....#...#.........#.#...#...#...#...#...#.#...#.....#.#.#...#.#...#.....#.........#...#.#...#.....#.#...#...#...#...#...#...#.#...#.#...#.#
#####.###.#####.#.#.#.###.#########.#.#.#.#.#######.###.#.#.#.#.#.#.#####.#.#######.###.#.#######.#.#.###.#.###.#.#####.###.#.#.#.#.#.#.###.#
#...#.#.#.....#.#.#...#.....#.......#.....#.........#...#.#...#...#...#...#...#...#...#.#...#.....#.#.....#.#...#.....#.#...#...#.#...#.#...#
#.#.#.#.#####.###.#####.###.#####.#########.#.#####.#.###.#.#.#######.#.#####.#.#####.#.###.#.#.###.#.#.###.#.#.#######.#.#####.#######.#.###
#.................#.....#.#.......#.....#...#.....#.#.#.#...#...#...#.#.......#.....#.#.....#.....#.#.#.....#.#.#.....#...#...#.#.......#...#
#############.#.#####.###.#########.###.#.#######.#.#.#.#.#####.#.#.#.#######.#####.#.#####.#######.#.###.###.###.###.#.###.#.#.#.#.#######.#
#.....#.....#.#.#...#.#.........#.....#.#.#.#.....#.#.#...#...#...#.#.......#.......#.....#.#...#...#...#...#...#.#...#.#...#.#.#.#.#.......#
#.###.#.###.#.#.#.#.#.#.#######.#.###.###.#.#.###.###.#####.#.###.###.#####.#.###########.###.#.#.#####.###.###.#.#.###.#.###.###.###.#####.#
#.#.#.#.#.#...#...#...#.#.....#...#...#...#.#.#...#...#.....#.#...#...#...#...#.....#.....#...#.#...#.#...#.....#.#.....#.#.....#.#...#.#...#
#.#.#.#.#.###.#.#######.#.#.#######.#.#.###.#.#####.###.#####.#.###.#####.###.#.###.#.#####.###.###.#.###.#######.#######.#####.#.#.###.#.###
#.#.....#...#.#.....#...#.#.....#.#...#...#.#...#...#...#...#.#...#.....#.....#...#.#.....#.#.....#.#...#.........#.....#.....#...#...#.#...#
#.#######.#.#.#.#.#.#.#######.#.#.#.#.###.#.###.#.###.#.#.#.#.#######.#.#####.###.#.#####.#.#.#####.###.###########.###.#####.###.###.#.###.#
#...#...#.#.#...#.#.#.........#...#.#...#.#...#...#...#...#.#.#.....#.#.....#...#.#.....#...#.#...#.....#...#.........#...................#.#
#.#.#.###.#.#####.#.###############.###.#.###.#############.#.#.###.#.###.#.#####.#####.#####.#.#.#####.#.###.#########.#####.#.#.#######.#.#
#.#.#.....#.......#...#...........#.#...#...........#.......#...#.......#.#.#.....#...#.....#...#.....#.#.#...#.........#...#.#.......#...#.#
#.#.#.#########.#####.#.#########.#.#######.#######.#.#.#.#######.#####.###.#.#####.#.###.#.#########.#.#.#.###.#####.###.#.###.#.###.#####.#
#.#.......#...#.....#...#.........#.#.......#...#...#.#.#...#...#...#.....#...#...#.#.#...#.#...#.#...#.#.#.#.#...#...#...#.....#...........#
#.#.#####.#.#.###.#######.#########.#.#######.#.#.###.#.###.#.###.#.#.#.#.#.###.#.###.#.###.#.#.#.#.###.#.#.#.###.###.#.#########.###########
#...#.....#.#...#...#...#...#.......#.....#...#.#.....#.....#.#...#...#.#.#.....#...#.#...#...#.#.#.....#...#...#...#.#.#...#.....#.........#
#.###.#########.###.#.#.###.#.#####.###.#.#.###.#.###########.#.#######.#.#########.#.###.#####.#.#######.###.#.###.###.#.###.###.#.#######.#
#.#.#.#.......#...#...#.....#...#.....#.#.#...#.#.#...#...........#...#.#.......#.#.#...#.#.........#.....#.....#...#.......#.............#.#
#.#.#.###.#.#.###.#####.###.###.#.#.###.#.###.#.###.#.#.#.###.#####.#.#.#######.#.#.#.#.#.###########.###.#.#####.#.#.###.#.#.###.#.###.###.#
#.#.....#.#.#.....#.......#.........#...#.#...#.....#...#...#...#...#...#.....#.......#.#.....#.......#.....#.....#.#.#...#.......#...#...#.#
#.#####.###.#######.#####.#.#######.#.###.#.###############.###.#.#######.#.#.#.###########.#.#.#######.###.#.#####.#.###.#######.###.###.#.#
#...#.#...#.....#...#...#.#.#.....#.#.#...#...#.....#...#...#...#.#.#.....#...#...........#.#.....#.....#...#...#.#.#...#...#.......#.#...#.#
###.#.###.#.###.#.###.###.###.#.#.###.#.#.###.#.#.#.###.#.###.###.#.#.#.###.#####.#######.#######.#.#####.#####.#.#.###.#####.###.###.#.#.#.#
#...#...#...#.#.#.#.....#.#...#.#.....#.#...#.#.#.#...#.#...#.#...#.#.#...#.#...#.......#.#.....#...#.........#.#...#.#.....#.#.#...#...#.#.#
#.#####.#.#.#.#.#.#.###.#.#.###.#######.#####.#.#.###.#.###.###.###.#.###.###.#.#.###.###.#.###.###########.###.#.###.#####.#.#.###.#####.#.#
#.....#...#...#.#.#.#...#.#.#...........#.......#.#.#.#...#.....#.......#.....#...#...#...#.#.#.#.........#.#...#...#.....#...#.#...#.....#.#
#####.#.#####.#.#.#.#.###.#.###.#.###.###.#######.#.#.#.#.#############.###########.###.###.#.#.#.#######.###.#####.#.#.#######.#.###.#####.#
#.....#.#.....#.#.#.#.......#...#...#.#...#.......#...#.#.#.........#.......#.#...#.........#.....#.....#...#.....#...#.#.......#.........#.#
#.#####.#######.#.#####.#####.#.#.#.###.###.#.#####.#####.#.#.#####.#######.#.#.#.#################.###.###.#.#.#.#####.#.#####.###########.#
#.....#.......#.#.....#.........#.#.....#...#.....#.........#...#...#...#.....#.#.......#.........#...#...#.#...#...#.....#...#.....#.....#.#
#.###.#######.#.#####.#.#########.###############.#####.#######.#.###.#.#.#####.#######.#.#######.###.###.#.###.###.#.#####.#.#.#####.###.#.#
#...#...#.........#.#...#.........#...#.........#.#...#.....#...#.#...#.#.#...#...#.......#.....#...#...#.#.#.....#.....#...#.#.#.....#...#.#
###.###.#########.#.###.#.#########.#.#.#######.#.###.#####.#.###.#.###.###.#.#.#.###########.#.###.#.#.###.###########.#.#.###.#.#####.###.#
#.#...#.....#...#.....#.#.#.........#...#.....#...#...#...#...#...#...#.....#.#.#.......#.....#...#.#.....#.....#.....#...#.#...#.#.#...#...#
#.#.#.#####.#.#.#######.#.#.###.###########.#.#####.#.#.#######.#####.#######.#.#######.###.#######.#.###.#####.#.#.#.#######.#.#.#.#.###.###
#...........#.#.........#.#.#...#.........#.#.......#...#.............#.....#.#.......#.#...#.......#...#.....#...#.#.#.......#...#.........#
#.#.#.###.###.#########.#.#.#.###.#######.#######.#.#####.###.#########.#####.#########.#.#.#.###.#######.#########.#.#.#####.#.#.#.#######.#
#...#.#...#.......#.....#...#.......#.....#.......#.#...#.#.#.................#...#.....#...#...........#.........#...#...#.#.#.#...#.......#
#.###.#.###.#######.###.#.#########.#.#####.#.#######.#.#.#.#######.###.#.#####.#.#.#####.#.###########.#.#######.#.#####.#.#.#.#.###.#####.#
#...#.#.#.....#...#...#...#.....#...#.#.............#.#.....#...#.....#.#.......#.#.#...#.#.....#.......#.......#.#.......#...#.#.....#.#...#
###.#.###.#####.#.###.#####.###.#.###.#.#####.#.###.#.#######.#.#.###.#.#######.#.#.#.###.###.#.#.#############.#.#########.###.#.#####.#.#.#
#...#.#...#.....#...#.#.....#...#...#.#.#.....#...#...#...#...#.#.#.#...#.......#...#.......#.#.#.#...#.....#...#.......#.....#.#.....#.....#
#####.#.###.#######.#.#.###.#.#####.#.#.#.#######.#####.#.#.###.#.#.###.###.###.#############.#.#.#.#.#.#####.#######.#.#.#.###.#.###.#####.#
#.........#...#...#.......#.#...#.....#.#.........#.....#.#...#...#.....#...#.#.......#...#...#.#...#.#...#...#.......#...#.....#...#...#...#
#.#.#.#######.#.#.#########.###.#.#.#.#####.#######.#####.#.#.#####.#####.###.#######.#.#.#.###.#.###.###.#.#####.#.#.#####.###.#.#.###.#.#.#
#.#...........#.#...........#.#...#...#...#...........#...#.#...#.#...#.....#.#.....#...#...#.......#.#...#.....#.#.#.#.....#...#.....#.#...#
#.#.#.###########.#.#######.#.###.###.#.#.#.#####.#####.###.###.#.###.#####.#.#.#.###########.#######.#.###.###.#.#.#.#.#######.#.#####.#.#.#
#.#...#...........#...#...#.....#...#...#...#...#...#...#...#...#...#...#...#.#.#.........#...#.#.....#...#.....#...#.#.....#.....#.#...#.#.#
#.#.#.#.#######.###.#.#.#.#.###.###.#########.#.#####.#######.###.#####.#.###.#.#####.#####.###.#.#.###.#.#.#####.#########.#.#.#.#.#.###.#.#
#.....#.....#...#...#...#.....#...#.#.........#.......#.......#.........#.#...#.#...#.....#.#...#.#.....#...#.....#...#.....#...#...#.....#.#
#####.#######.###.#############.###.#.#################.###.#####.#.#####.###.#.#.#.#####.#.#.#.#.#########.#####.#.#.#.#####.#.#.#.#.#####.#
#...#.............#.......#.....#...#...........#.......#.#.#...#.......#...#...#.#.....#.#.....#.....#...#.......#.#...#...................#
#.###.#########.#####.###.#.###.#.#############.#######.#.#.#.#.#####.#.###.#.#########.#.#####.#####.#.#.#######.#.#.###.###.#.#.###.#.#.#.#
#.......#.....#.....#...#.#...#.#.#.......#.....#.......#.....#.....#.#.....#.#...#.....#.#...#.#.#...#.#.#.....#.#.......#.#...#.#...#.#...#
#.###.#.#.###.#####.###.#.###.#.#.#.#.###.#.###.#.###.#.#####.#####.#.#####.#.#.#.#.###.#.#.#.#.#.#.###.#.#.###.#.#########.#.#####.#.#.###.#
#.....#.#...#.....#.....#.#...#.....#...#...#.#...#.#.#.......#.....#.......#...#...#...#...#.#...#.#...#.#...#.#.....#.............#.#...#.#
#.#.#.#.###.#.#########.#.#.###.###.###.#####.#.#.#.#.#########.#####.#.#############.#######.###.#.###.#.#.#.#####.#.###.#.#.#######.###.###
#.........#.#...........#.#.#...#.#...#...#.....#.#.............#.#...#.....#...#...#.#.....#...#.#.....#.#.#...............#.#...#.....#...#
#.#.###.#.#.#######.#####.#.#.###.#.#####.#.#####.###############.#.#####.#.#.#.#.#.#.###.#####.#.#######.#.###################.#.#.#######.#
#...#...#.#...#...#.#.....#.#...#...#.....#.#.....#.......#.......#.#...#.#...#...#.....#.....#.#.....#...#.....#.........#...#.#.#.#.......#
#####.###.#.###.#.#.#.#####.###.#####.#####.#.#####.#####.#.###.###.#.#.#########.#.###.#####.#.###.#.#.#########.#######.#.#.#.#.###.#######
#.....#...#.#...#...#...#.#...#.......#...#.#.#.....#.#...#...#.#.....#...#...#.....#.#.#.....#...#...#.....#...#.....#.#.#.#.#.#...#.#.....#
#.#########.#.#.#######.#.#.###########.#.#.#.#.###.#.#.#####.###.###.###.#.#.#.###.#.#.#.#######.###.#####.#.#.#.###.#.#.#.#.#.###.#.#.###.#
#...#.......#.#.#.....#.#.#.#.......#.......#.#...#...#.#...#...#...#...#...#.....#.#.#.#.......#.........#...#.#.....#.....#.#.#...#.#...#.#
###.#.#####.#.###.###.#.#.#.#.#####.#.#######.###.###.#.#.#.###.###.###.###########.#.#.#####.#.###############.#.#####.#####.#.###.#.###.#.#
#...................#.#...#.#...#.....#.....#...#.#...#...#...#.....#.#...#.#...#...#.#.......#.....#...........#.#.......#...#...#...#...#.#
#.#####.###.#########.###.#.###.#.###.#.###.###.#.#.#########.###.###.###.#.#.#.#.###.###.#.#######.#.###########.#####.#.#.#####.#####.###.#
#.....#...#.......#.....#.......#.#...#...#.#.#...#.#.......#...#.......#...#.#...#.........#.....#.#.....#.......#...#.#.#.....#.........#.#
###.###.#.#.#####.#.###.#.#######.#.#####.#.#.#####.#.#.#.#.###.#######.###.#.#####.#########.###.#######.#.#.###.#.#.#.#.#####.#########.#.#
#...#.....#...#...#...#.#.#.....#...#.....#...#...........#.#...#...#...#...#...#.#.#.........#...#.....#...#.....#.#.#.#.#.............#.#.#
#.#.#.#.###.#.#######.#.#.###.#######.#.#######.#########.#.#.###.#.#.###.#####.#.#.#.#########.#.#.#.#.###.#####.#.#.###.#.#.#########.###.#
#.#.#.#.......#.......#.#...#.#.....#.#.....#...#...#.....#.#.....#.............#...#.....#...#.#.#.#.#.....#...#...#...#...#...#.....#.....#
#.#.#.#.#.#.#.#.#######.###.#.#.#.#.#######.#.#####.#.###.#######.#####.###.#####.#######.#.#.#.###.#.###.###.#.#.###.#.#####.#.#.#########.#
#.#.#...#.#.#.#.#.......#...#.#.#.#.........#.......#.#...#.....#.........#.....#.#...#.#.#.#.#...#.#.#...#...#.#...#...#...#.#.#...#.....#.#
#.#####.###.#.#.#.#######.###.#.#.###############.###.#####.###.#.#########.###.#.#.#.#.#.#.#####.#.#.#.###.###.#.#.#.###.#.#.#.#.#.#.###.#.#
#.......#...#.#.#...#...#...#.........#.....#...#.#...#...#.#.#...........#...#...............................#.#.........#...#.#.#.#.#.#...#
#.#####.#.#.#.#.#####.#.###.#####.###.#.###.#.#.#.#.###.#.#.#.###.#######.#####.#####.#.#.###.###.#.#######.#.#.#.###.#######.#.###.#.#.#####
#.#.......#.#...#...#.#.....#...#...#.#...#...#...#.#...#...#...........................#...#.......#.......#.#.#.............#...#.#.......#
#.#.###.#.#.#.#.#.#.#.#######.#.###.#.###.#####.###.#.#########.#.###.###.#.#######.###.###.###.#######.#####.#.#.###.###########.#.#######.#
#...#.....#...#.#.#...#.......#...#.#.#...........#.#.........#.#...#.......#.....#.....#...#...#.....#.#.#.....#.....#.......#...#.........#
#.#.#.#.###.#.###.#########.#####.#.#.#.###########.#.#######.#.#.#.#########.###.#####.#.###.#.#.###.#.#.#.#####.###.#.#####.#.###.#########
#...#.....#.#.#...#.....#...#...#.#.#.....#...#...#.......#...#...#.......#...#.#.#.....#.....#.#.#.#.#.#.#...#...........................#.#
#########.#.###.#####.#.#.###.#.#.#######.#.#.#.#.###.###.#.#####.#########.###.#.#############.#.#.#.#.#.###.#####.#.###.#.###.#.#.#.###.#.#
#S........#...........#...#...#.............#...#.........#.....................#.................#.....#...........#...........#.....#.....#
#############################################################################################################################################""".splitlines()
