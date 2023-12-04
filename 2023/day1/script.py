
f = open('2023/day1/sample.txt')
# f = open('2023/day1/data.txt')

# rows = f.read().split('\n')
rows = tuple(line.strip() for line in f)
print(rows)

f.close()

# ----------------------------- #
# [part 1]

# total = 0
# for row in rows:
#     print(row)
#     digits = [c for c in row if c.isdigit()]
#     n = int(digits[0] + digits[-1])
#     print(n)
#     total += n

# print(total)


# ----------------------------- #
# [part 2]

digits = "123456789"
names = "one two three four five six seven eight nine".split()

lookup = {}
lookup.update(zip(digits, digits))
lookup.update(zip(names, digits))

def score(row):
    found = []
    for i in range(len(row)):
        tail = row[i:]

        for key, value in lookup.items():
            if tail.startswith(key):
                found.append(value)
                break
    
    return int(found[0] + found[-1])

print(sum(score(row) for row in rows))