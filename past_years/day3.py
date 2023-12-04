
trees = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''.strip().split('\n')

row = 0
col = 0

total = 0
while True:
    col += 3
    col %= len(trees[0])
    row += 1

    if trees[row][col] == '#':
        total += 1
        print(total)




