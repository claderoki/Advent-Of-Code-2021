from collections import Counter

from .helpers import *

path = __file__.replace("\\", "/").replace("__main__.py", "")

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
    least.append("1" if common == "0" else "0")

gamma   = int("".join(most), 2)
epsilon = int("".join(least), 2)
print(gamma * epsilon)

print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
print('--- PART 2 (END) ---')
