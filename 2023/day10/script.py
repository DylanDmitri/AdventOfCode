import re
from collections import Counter, defaultdict

def blap(pattern, row):
    return re.findall(pattern, row)

def mcast(row, func):
    return [func(i) for i in row.strip().split()]

p = print

f = open('2023/day10/sample.txt')
f = open('2023/day10/data.txt')

rows = tuple(line.strip() for line in f.read().split('\n'))
if not rows: print('EMPTY'); quit()
f.close()

# ------------------------ #

map_lookup = {}
lead_cells = []

for row_idx, row in enumerate(rows):
    for col_idx, char in enumerate(row):
        coord = row_idx + 1j*col_idx
        map_lookup[coord] = char
        if char == 'S':
            lead_cells = [ coord ]

up, down, left, right = [
    -1 + 00, +1 + 00,
    00 - 1j, 00 + 1j,
]
pipe_maps = {
    '|': (up, down),
    '-': (left, right),
    'L': (up, right),
    'J': (up, left),
    '7': (left, down),
    'F': (right, down),
    '.': (),
    'S': (up, down, left, right)
}

theloop = set(lead_cells)

def build_loop():
    global theloop, lead_cells

    step = 0
    while True:
        step += 1
        # print(next_stops)
        # input()
        new_stops = []
        for coord in lead_cells:
            char = map_lookup.get(coord, '.')
            # print(char, '@', coord)
            for offset in pipe_maps[char]:
                candidate = coord + offset
                target_char = map_lookup.get(candidate, '.')
                target_connections = pipe_maps[target_char]

                if -offset not in target_connections:
                    continue

                if candidate not in theloop:
                    if candidate in new_stops:
                        print('found!', candidate)
                        print('step', step)
                        theloop.update(new_stops)
                        return candidate

                    new_stops.append(candidate)
        
        theloop.update(new_stops)
        lead_cells = new_stops

build_loop()


space_in_loop = 0

for row_idx, row in enumerate(rows):

    parity = 0

    row_blobs = []
    edge_start = None

    for col_idx, char in enumerate(row):
        coord = row_idx + 1j*col_idx

        if char == 'S':
            char = '|'

        if coord not in theloop:
            if parity % 2 == 1:
                p(coord)
                space_in_loop += 1

        elif char == '|':
            parity += 1
        
        elif char in 'FL7J':
            if edge_start is None:
                edge_start = char
            else:
                # if edge_start and current same up
                #    like F and 7  or   J and L
                # they don't count
                if {edge_start, char} in ({'F', '7'}, {'J', 'L'}):
                    parity += 0
                else:
                    parity += 1
                edge_start = None





print(space_in_loop)


# flood fill below
quit()

rowbounds = (0, len(rows)-1)
colbounds = (0, len(rows[0])-1)

checknext = set()
filled = set()

for rownum in rowbounds:
    for colnum in range(*colbounds):
        checknext.add(rownum + 1j*colnum)

for colnum in colbounds:
    for rownum in range(*rowbounds):
        checknext.add(rownum + 1j*colnum)

checknext = {spot for spot in checknext if spot not in theloop}

while True:
    newest_spots = set()
    for spot in checknext:
        for offset in (up, down, left, right):
            candidate = spot + offset
            if candidate in theloop:
                continue
            if candidate not in map_lookup:
                continue
            if candidate in filled:
                continue
            newest_spots.add(candidate)
        
    if len(newest_spots) == 0:
        break

    filled.update(newest_spots)
    checknext = newest_spots

print(len(theloop))
print(len(filled))

    









