from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

positions = [int(x) for x in data.split(',')]

def get_fuel_cost(position: int, acceleration: bool) -> int:
    total = 0
    for x in positions:
        distance = abs(x-position)
        if acceleration:
            for i in range(1, distance+1):
                total += i
        else:
            total += distance
    return total

def get_min_cost(acceleration: bool) -> int:
    costs = []
    for i in range(max(positions)):
        cost = get_fuel_cost(i, acceleration)
        costs.append(cost)

    return min(costs)

print('--- PART 1 (START) ---')
print(get_min_cost(False))
print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
print(get_min_cost(True))
print('--- PART 2 (END) ---')