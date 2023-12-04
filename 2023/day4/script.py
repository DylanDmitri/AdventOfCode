
f = open('2023/day4/sample.txt')
f = open('2023/day4/data.txt')

rows = tuple(line.strip() for line in f)

f.close()

# ------------------------ #

def cast(row):
    return {int(i) for i in row.strip().split()}

def parse(row):
    _, nums = row.split(':')
    winning, yours = nums.strip().split('|')

    winning = cast(winning)
    yours = cast(yours)

    return winning, yours

print(rows)
rows = [parse(row) for row in rows]

total = 0
for winning, yours in rows:
    common = winning.intersection(yours)
    print(common)

    points = 0
    if common:
        points = 2 ** (len(common)-1)

    print(points)
    total += points

print(total)

# p2

matches = [
    len(a.intersection(b))
    for a, b in rows
]

copies = [1 for _ in range(len(rows))]


for i, num in enumerate(matches):
    dx = copies[i]

    for j in range(i+1, i+1+num):
        copies[j] += dx

print(copies)
print(sum(copies))



