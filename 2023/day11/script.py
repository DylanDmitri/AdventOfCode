from itertools import combinations

f = open('2023/day11/sample.txt')
f = open('2023/day11/data.txt')

rows = tuple(line.strip() for line in f.read().split('\n'))

# ------------------------ #

cols = [
    ''.join(column)
    for column in zip(*rows)
]

ex_rows = [
    idx
    for idx, row in enumerate(rows)
    if tuple(set(row)) == ('.',)
]
ex_cols = [
    idx
    for idx, col in enumerate(cols)
    if tuple(set(col)) == ('.',)
]

exp_factor = 1_000_000
exp_factor -= 1

def distance(start, end):
    row_bounds = sorted((start[0], end[0]))
    col_bounds = sorted((start[1], end[1]))

    row_dist = row_bounds[1] - row_bounds[0]
    col_dist = col_bounds[1] - col_bounds[0]

    row_exp = sum(
        exp_factor for idx in ex_rows
        if row_bounds[0] < idx < row_bounds[1]
    )
    col_exp = sum(
        exp_factor for idx in ex_cols
        if col_bounds[0] < idx < col_bounds[1]
    )

    return row_dist + col_dist + row_exp + col_exp

# p(distance((5, 1), (9, 4)))

galaxies = []
for row_idx in range(len(rows)):
    for col_idx in range(len(cols)):
        if rows[row_idx][col_idx] == '#':
            galaxies.append((row_idx, col_idx))

total = 0
for pair in combinations(galaxies, 2):
    total += distance(*pair)

print(total)
