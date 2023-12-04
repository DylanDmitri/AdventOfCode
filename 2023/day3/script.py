
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

pnums = []

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
                    pnums.append(number)

                cstart = None
    
    if cstart is not None:
        cend = j+1
        number = line[cstart: cend]

        print(number, grid[cstart: cend])

        if '#' in grid[cstart: cend]:
            pnums.append(number)



    


print(sum(
    [int(p) for p in pnums]
))


