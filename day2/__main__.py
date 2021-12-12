from .helpers import Command, Position

path = __file__.replace("\\", "/").replace("__main__.py", "")

with open(f'{path}/input') as f:
    data = f.read()

commands = [Command.from_raw(x) for x in data.splitlines()]

print('--- PART 1 (START) ---')
position = Position()
for command in commands:
    if command.direction == Command.Direction.down:
        position.depth += command.amount
    elif command.direction == Command.Direction.up:
        position.depth -= command.amount
    elif command.direction == Command.Direction.forward:
        position.horizontal += command.amount

print(position.depth * position.horizontal)
print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
position = Position()
for command in commands:
    if command.direction == Command.Direction.down:
        position.aim += command.amount
    elif command.direction == Command.Direction.up:
        position.aim -= command.amount
    elif command.direction == Command.Direction.forward:
        position.horizontal += command.amount
        position.depth      += position.aim * command.amount

print(position.depth * position.horizontal)
print('--- PART 2 (END) ---')