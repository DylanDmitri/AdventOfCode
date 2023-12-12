import re
from collections import Counter, defaultdict

def blap(pattern, row):
    return re.findall(pattern, row)

def mcast(row, func):
    return [func(i) for i in row.strip().split()]

p = print

# f = open('2023/day6/sample.txt')
f = open('2023/day6/data.txt')

rows = tuple(line.strip() for line in f.read().split('\n'))
if not rows: print('EMPTY'); quit()
f.close()

# ------------------------ #

"""
2: 0, 1, 0
3: 0, 2, 2, 0
4: 0, 3, 4, 3, 0
5: 0, 4, 6, 6, 4, 0

d2: +1 -1
d3: +2 00 -2
d4: +3 +1 -1 -3
d5: +4 +2 00 -2 -4

"""

def scoresfor(limit):
    delta = limit-1
    prior = 0
    yield prior

    for _ in range(limit):
        prior = prior + delta
        yield prior
        delta -= 2
    
print(scoresfor(7))

def ways2beat(limit, record):
    return sum(o > record for o in scoresfor(limit))

print(ways2beat(15, 40))

times = map(int, blap('\d+', rows[0]))
records = map(int, blap('\d+', rows[1]))

v = []
for t, r in zip(times, records):
    v.append(ways2beat(t, r))

print(v)

p = 1
for i in v:
    p *= i
print(p)

def bignum(s):
    return int(''.join(c for c in s if c.isdigit()))
    # s.filter(isdigit).join().as(Int)

time = bignum(rows[0])
distance = bignum(rows[1])

print(time, distance)

print(ways2beat(time, distance))
