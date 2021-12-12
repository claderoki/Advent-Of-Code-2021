from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

positions = []
for line in data.splitlines():
    sides  = line.split(' -> ')
    x1, y1 = sides[0].split(',')
    x2, y2 = sides[1].split(',')
    pos1 = Position(int(x1), int(y1))
    pos2 = Position(int(x2), int(y2))
    positions.append((pos1, pos2))

SIZE = 10
rows = [[Cell() for _ in range(SIZE)] for _ in range(SIZE)]

def increment(start: Position, end: Position):
    if start.x != 9:
        return

    print(start, end)
    for i in range(start.x, end.x + 1, (-1 if start.x > end.x else 1)):
        print(i, end = ', ')
        rows[start.y][i].count += 1
    print()

    for i in range(start.y, end.y + 1, (-1 if start.y > end.y else 1)):
        print(i, end = ', ')
        rows[i][start.y].count += 1
    print()

for start, end in positions:
    if start.x == end.x or start.y == end.y:
        increment(start, end)
        # break

for row in rows:
    print("".join([str(x) for x in row]))

print('--- PART 1 (START) ---')
print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
print('--- PART 2 (END) ---')