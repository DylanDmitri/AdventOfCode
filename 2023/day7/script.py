import re
from collections import Counter, defaultdict

def blap(pattern, row):
    return re.findall(pattern, row)

def mcast(row, func):
    return [func(i) for i in row.strip().split()]

p = print

f = open('2023/day7/sample.txt')
f = open('2023/day7/data.txt')

rows = tuple(line.strip() for line in f.read().split('\n'))
if not rows: print('EMPTY'); quit()
f.close()

# ------------------------ #

lookup = dict(zip('TJQKA', range(10, 10+5)))
def cardnum(card):
    return lookup.get(card) or int(card)

# part1
# def value(hand):
#     cards = tuple(cardnum(c) for c in hand) 
#     val = sorted(tuple(Counter(cards).values()), reverse=True)
#     return (val, cards)

# part2

lookup['J'] = 1

def value(hand):
    cards = tuple(cardnum(c) for c in hand) 
    groups = sorted(list(Counter(cards).values()), reverse=True)

    num_jokers = cards.count(1)
    if num_jokers and len(groups) > 1:
        groups.remove(num_jokers)
        groups[0] += num_jokers

    return (groups, cards)

# for row in rows:
#     h = row.split()[0]
#     p(h, value(h))

# final solve
rows = [
    (value(row.split()[0]), int(row.split()[1]))
    for row in rows
]

total = sum((
    (i+1) * (row[1])
    for (i, row) in enumerate(sorted(rows))
))

p(total)
