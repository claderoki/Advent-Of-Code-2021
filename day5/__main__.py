from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

def debug_rows(rows: list):
    for row in rows:
        print("".join([str(x) for x in row]))

positions = []
for line in data.splitlines():
    sides  = line.split(' -> ')
    x1, y1 = sides[0].split(',')
    x2, y2 = sides[1].split(',')
    pos1 = Position(int(x1), int(y1))
    pos2 = Position(int(x2), int(y2))
    positions.append((pos1, pos2))

def init_rows(size: int) -> list:
    return [[Cell() for _ in range(size)] for _ in range(size)]

def __range(start, end) -> range:
    if start > end:
        step = -1
        end -= 1
    else:
        step = 1
        end += 1

    return range(start, end, step)

def __increment_horizontally(rows: list, start: Position, end: Position):
    row = start.y
    for cell in __range(start.x, end.x):
        rows[row][cell].count += 1

def __increment_vertically(rows: list, start: Position, end: Position):
    cell = end.x
    for row in __range(start.y, end.y):
        rows[row][cell].count += 1

def __increment_diagonally(rows: list, start: Position, end: Position):
    y = list(__range(start.y, end.y))
    for index, x in enumerate(__range(start.x, end.x)):
        cell = x
        row  = y[index]
        rows[row][cell].count += 1

def increment(rows: list, start: Position, end: Position):
    if start.x == end.x:
        __increment_vertically(rows, start, end)
    elif start.y == end.y:
        __increment_horizontally(rows, start, end)
    else:
        __increment_diagonally(rows, start, end)

def count_overlap(rows):
    overlap = 0
    for row in rows:
        for cell in row:
            if cell.count > 1:
                overlap += 1
    return overlap

SIZE = 999

print('--- PART 1 (START) ---')

rows = init_rows(SIZE)
for start, end in positions:
    if start.x != end.x and start.y != end.y:
        continue
    increment(rows, start, end)

print(count_overlap(rows))

print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')

rows = init_rows(SIZE)
for start, end in positions:
    increment(rows, start, end)

print(count_overlap(rows))

print('--- PART 2 (END) ---')