
def getRecords(row):
    data = row.split(":")[1]
    data = data.replace(';', ',').split(',')

    records = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for record in data:
        num, name = record.split()
        records[name] = max(records[name], int(num))
    
    return records


f = open('2023/day2/sample.txt')
f = open('2023/day2/data.txt')

rows = tuple(line.strip() for line in f)
records = [getRecords(row) for row in rows]

for record in records:
    print(record)

def valid(record):
    return not any((
        record['red'] > 12,
        record['green'] > 13,
        record['blue'] > 14,
    ))

for record in records:
    print(valid(record))

print('PART 1 --')

print(sum(
    (idx+1) for idx, r in enumerate(records)
    if valid(r)
))

print('PART 2 --')

print(sum(
    record['red'] * record['green'] * record['blue']
    for record in records
))





