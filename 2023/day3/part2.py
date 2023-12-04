
f = open('2023/day3/sample.txt')
f = open('2023/day3/data.txt')

rows = tuple(line.strip() for line in f)

f.close()

# ------------------------ #

def symbol_cords(row):
    r = []
    for i, c in enumerate(row):
        if c.isdigit():
            continue
        elif c == '.':
            continue
        else:
            r.append(i)
    return r

    
symbols = {
    i: symbol_cords(row) 
    for i, row in enumerate(rows)
}

def showmarks(marks):
    r = ['.']*(len(rows[0])+1)
    for m in marks:
        r[m] = '#'
        r[m-1] = '#'
        r[m+1] = '#'
    return ''.join(r)

numbersat = {}
def load(rownum, start, end, value):
    for colnum in range(start, end):
        numbersat[rownum, colnum] = (value, rownum, start)

for i, line in enumerate(rows):
    marks = symbols.get(i-1, []) + symbols.get(i, []) + symbols.get(i+1, [])
    grid = showmarks(marks)
    print(grid)

    cstart = None

    for j, c in enumerate(line):
        if c in '1234567890':
            if cstart is None:
                cstart = j
            else:
                pass  # number extends

        else:
            if cstart is not None:
                cend = j
                number = line[cstart: cend]

                print(number, grid[cstart: cend])

                if '#' in grid[cstart: cend]:
                    load(i, cstart, cend, int(number))

                cstart = None
    
    if cstart is not None:
        cend = j+1
        number = line[cstart: cend]

        print(number, grid[cstart: cend])

        if '#' in grid[cstart: cend]:
            load(i, cstart, cend, int(number))

print(numbersat)

# {0,3: 467}

joined = []

for x, row in enumerate(rows):
    r = []
    for y, c in enumerate(row):
        if c.isdigit():
            continue
        elif c == '.':
            continue
        else:
            adj = set()
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    v = numbersat.get((x+dx, y+dy))
                    if v:
                        adj.add(v)
            # x y
            joined.append(adj)


total = 0
for group in joined:
    if len(group) == 2:

        scores = [label[0] for label in group]
        total += scores[0] * scores[1]

print(total)
    



