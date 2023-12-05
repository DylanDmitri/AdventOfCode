import re
from collections import Counter, defaultdict

def blap(pattern, row):
    return re.findall(pattern, row)

def mcast(row, func):
    return [func(i) for i in row.strip().split()]

p = print

f = open('2023/day5/sample.txt')
f = open('2023/day5/data.txt')

rows = tuple(line.strip() for line in f.read().split('\n\n'))
if not rows: print('EMPTY'); quit()
f.close()

# ------------------------ #

class OffsetRange:
    def __init__(self, line):
        drange, srange, rangel = map(int, line.split())
        self.offset = drange - srange
        self.start = srange
        self.end = rangel + srange
    
    def __repr__(self):
        return f'{self.start}-{self.end} by {self.offset}'

class Mapping:
    def __init__(self, para):
        lines = para.split('\n')
        self.title = lines[0].split()[0]
        self.a, self.b = self.title.split('-to-')

        self.index = {}

        self.offsets = [
            OffsetRange(line)
            for line in lines[1:]
        ]


    def lookup(self, i):
        for range in self.offsets:
            if range.start <= i <= range.end:
                return i + range.offset
        return i



seeds = rows[0].split(': ')[1].split()
seeds = [int(s) for s in seeds]

rr = [Mapping(row) for row in rows[1:]]

# for r in rr:
#     p(r.a, r.b)

def runseed(seed):
    results = [seed]
    for transform in rr:
        j = transform.lookup(results[-1])
        results.append(j)
    return results

def location(seed):
    return runseed(seed)[-1]


def p2seeds():
    for a,b in zip(seeds[::2], seeds[1::2]):
        yield from range(a, a+b)

# for r in rr:
#     for offset in r.offsets:
#         print(offset.offset)
#     p()



course = []
for r in rr:
    stage = None

    offsets = sorted(r.offsets, key=lambda o: o.start)
    bands = []
    if offsets[0].start > 0:
        bands.append((0, 0))

    for i, offset in enumerate(offsets):
        if bands and bands[-1][0] == offset.start:
            bands[-1] = (offset.start, offset.offset)
        else:
            bands.append((offset.start, offset.offset))
        bands.append((offset.end, 0))
        
    p(bands)
    course.append(bands)

class Slice:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f'{self.start}-{self.end}'

def use(slice, bands ):
    # p(slice)
    # p(bands)
    splits = [slice.start]

    for band in bands:
        if slice.start <= band[0] < slice.end:
            splits.append(band[0])
    splits.append(slice.end)
    # p('splits', splits)
    
    band_idx = None
    for i, band in enumerate(bands):
        if band[0] > splits[0]:
            band_idx = i-1
            break
    
    startband = band_idx
    if band_idx is None:
        band_idx = len(bands) - 1



    out = []
    for a,b in zip(splits, splits[1:]):
        
        try:
            dx = bands[band_idx][1]
        except IndexError:
            p()
            p(startband)
            p(band_idx, len(bands))
            p(splits)
            quit()

        band_idx += 1

        out.append(Slice(a+dx, b+dx))
    
    return out






def p2seeds():
    r = []
    for a,b in zip(seeds[::2], seeds[1::2]):
        r.append(Slice(a, a+b))
    return r

p2 = p2seeds()

# use(test, course[0])

def percolate(seed, depth):
    # p()
    if depth >= len(course):
        # p('location', seed.start)
        return seed.start

    out = use(seed, course[depth])
    scores = [percolate(s, depth+1) for s in out]
    return min(scores)

test = Slice(82, 82)
test = (p2[1])

locs = [percolate(seed, 0) for seed in p2seeds()]
p(locs)
p(min(locs))

# p(min(map(location, p2seeds())))


