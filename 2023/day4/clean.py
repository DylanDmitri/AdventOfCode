import re
from collections import Counter

def blap(pattern, row):
    return re.findall(pattern, row)

def mcast(row, func):
    return [func(i) for i in row.strip().split()]

p = print

f = open('2023/day4/sample.txt')
# f = open('2023/day4/data.txt')

rows_raw = tuple(line.strip() for line in f)

f.close()

# ------------------------ #

def parse(row):
    nums = blap('\d+', row)[1:]
    c = Counter(nums)
    return tuple(c.values()).count(2)

rr = [parse(row) for row in rows_raw]

def score1(hits):
    if hits == 0: return 0
    return 2 ** (hits-1)

for pp in rr:
    p(pp, score1(pp))

p(sum(map(score1, rr)))


copies = [1 for _ in rr]

for i, num in enumerate(rr):
    dx = copies[i]

    for j in range(i+1, i+1+num):
        copies[j] += dx

p(copies)
p(sum(copies))



