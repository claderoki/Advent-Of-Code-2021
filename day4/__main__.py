from .helpers import *

path = __file__.replace('\\', '/').replace('__main__.py', '')

with open(f'{path}/input') as f:
    data = f.read()

lines = data.splitlines()

print('--- PART 1 (START) ---')
def find_first_winner(numbers, boards) -> WinningResult:
    for number in numbers:
        for board in boards:
            for row in board.rows:
                for cell in row:
                    if cell.value == number:
                        cell.mark()
        
            if board.has_winning_condition():
                return WinningResult(board, number)

numbers = [int(x) for x in lines[0].split(',')]
boards  = [Board.from_raw(x) for x in data.split('\n\n')[1:]]
result  = find_first_winner(numbers, boards)
unmarked = sum([sum([j.value for j in x if not j.marked]) for x in result.board.rows])
print(unmarked * result.number)

print('--- PART 1 (END) ---')

print('--- PART 2 (START) ---')
def find_last_winner(numbers, boards) -> WinningResult:
    results   = []
    for number in numbers:
        for board in boards:
            if board in [x.board for x in results]:
                continue

            for row in board.rows:
                for cell in row:
                    if cell.value == number:
                        cell.mark()
        
            if board.has_winning_condition():
                results.append(WinningResult(board, number))
    return results[-1]

numbers = [int(x) for x in lines[0].split(',')]
boards  = [Board.from_raw(x) for x in data.split('\n\n')[1:]]
result  = find_last_winner(numbers, boards)
unmarked = sum([sum([j.value for j in x if not j.marked]) for x in result.board.rows])
print(unmarked * result.number)

print('--- PART 2 (END) ---')