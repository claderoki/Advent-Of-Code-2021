from collections import Counter

from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

lines  = data.splitlines()

print('--- PART 1 (START) ---')
column = [[] for _ in range(len(lines[0]))]

for line in lines:
    for index, char in enumerate(line):
        column[index].append(char)

least = []
most  = []

for row in column:
    counter = Counter(row)
    common  = counter.most_common(1)[0][0]
    most.append(common)
    least.append('1' if common == '0' else '0')

gamma   = int(''.join(most), 2)
epsilon = int(''.join(least), 2)
print(gamma * epsilon)

print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')

def get_most_common(counter: Counter) -> str:
    if counter['0'] == counter['1']:
        return '1'

    return counter.most_common(1)[0][0]

def get_common(counter: Counter, type: str) -> str:
    most_common = get_most_common(counter)
    if type == 'least':
        return '0' if most_common == '1' else '1'
    else:
        return most_common

def get_valid_rows(rows: list, index: int, type: str):
    counter = Counter()
    for row in rows:
        char = row[index]
        counter[char] += 1

    common = get_common(counter, type)
    return [x for x in rows if x[index] == common]

width  = len(lines[0])
oxygen = lines
co2    = lines
for i in range(width):
    if len(oxygen) > 1:
        oxygen = get_valid_rows(oxygen, i, 'most')
    if len(co2) > 1:
        co2    = get_valid_rows(co2, i, 'least')

print(int(oxygen[0], 2) * int(co2[0], 2))

print('--- PART 2 (END) ---')
