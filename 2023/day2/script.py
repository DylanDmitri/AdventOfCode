
f = open('2023/day2/sample.txt')
f = open('2023/day2/data.txt')

# rows = f.read().split('\n')
rows = tuple(line.strip() for line in f)

f.close()

# ------------------------ #
# [part 1]

class Game:
    def __init__(self, text):
        label, rest = text.split(':')
        _, self.ID = label.split()
        self.ID = int(self.ID)

        self.draws = [Draw(t) for t in rest.split(';')]
    
    def valid_p1(self):
        for draw in self.draws:
            if any([draw.red > 12, draw.green > 13, draw.blue > 14]):
                return False
        return True
    
    def fewest_set(self):
        return [
            max(d.red for d in self.draws),
            max(d.blue for d in self.draws),
            max(d.green for d in self.draws),
        ]


class Draw:
    def __init__(self, text):
        self.red = 0
        self.blue = 0
        self.green = 0

        for item in text.split(','):
            number, name = item.split()
            setattr(self, name, int(number))


games = [Game(row) for row in rows]

print(sum(
    game.ID for game in games if game.valid_p1()
))

total = 0
for game in games:
    f = game.fewest_set()
    print(f)
    total += f[0]*f[1]*f[2]
print(total)


