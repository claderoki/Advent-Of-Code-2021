from collections import Counter

from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

NEW_TIMER   = 8
RESET_TIMER = 6

def count_fish(days: int, debug: bool = False) -> int:
    fishes = {x:0 for x in range(NEW_TIMER+1)}

    for value in data.split(','):
        fishes[int(value)] += 1

    if debug:
        print(f'Initial state:\t{sum(fishes.values())} fishes')

    day = 1
    while day <= days:
        previously_added = 0
        for current_index in range(len(fishes)-1, -1, -1):
            current_count = fishes[current_index] - previously_added

            if current_index == 0:
                new_index    = RESET_TIMER
                new_to_spawn = current_count
            else:
                new_index    = current_index - 1
                new_to_spawn = 0

            if new_to_spawn > 0:
                fishes[NEW_TIMER] += new_to_spawn

            fishes[new_index]    += current_count
            fishes[current_index] = previously_added
            previously_added      = current_count

        if debug:
            print(f'After {day} days:\t{sum(fishes.values())} fishes')

        day += 1

    return sum(fishes.values())

print('--- PART 1 (START) ---')
print('After 80 days', count_fish(80))
print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
print('After 256 days', count_fish(256))
print('--- PART 2 (END) ---')