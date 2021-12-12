with open('input') as f:
    data = f.read()

lines = [int(x) for x in data.splitlines()]

print('--- PART 1 (START) ---')
increases = 0
previous  = None
for line in lines:
    if previous is not None and line > previous:
        increases += 1
    previous = line

print(increases)
print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
WINDOW    = 3
previous  = None
increases = 0
for i in range(len(lines)):
    if i < WINDOW-1:
        continue

    amount = sum(lines[i-WINDOW:i])
    if previous is not None and amount > previous:
        increases += 1
    previous = amount

print(increases)
print('--- PART 2 (END) ---')