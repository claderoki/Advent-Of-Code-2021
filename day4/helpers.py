class Base:
    __slots__ = ()

    def __str__(self):
        return ', '.join(f'{x} => {getattr(self, x)}' for x in self.__slots__)

    def __repr__(self):
        return str(self)

class Cell(Base):
    __slots__ = ('value', 'marked')

    def __init__(self, value: int):
        self.value  = value
        self.marked = False
    
    def mark(self):
        self.marked = True

class Board(Base):
    __slots__ = ('rows', )

    def __init__(self, rows: list):
        self.rows = rows

    @classmethod
    def from_raw(cls, raw) -> 'Board':
        rows = [[Cell(int(j)) for j in x.split() if j != ''] for x in raw.splitlines()]
        return cls(rows)

    def __is_winning_column(self, index: int) -> bool:
        x = 0
        for row in self.rows:
            cell = row[index]
            if cell.marked:
                x += 1

        return x == len(row)

    def debug_string(self) -> str:
        lines = []
        for row in self.rows:
            rows = []
            for cell in row:
                rows.append(str((cell.value if cell.marked else '--')).zfill(2))
            lines.append(' '.join(rows))
        return '\n'.join(lines)

    def __is_winning_row(self, row: list) -> bool:
        x = 0
        for cell in row:
            if cell.marked:
                x += 1

        return x == len(row)

    def has_winning_condition(self) -> bool:
        for i, row in enumerate(self.rows):
            if self.__is_winning_row(row):
                return True

            if i == 0:
                for index in range(len(row)):
                    if self.__is_winning_column(index):
                        return True

        return False

class WinningResult(Base):
    __slots__ = ('board', 'number')

    def __init__(self, board: Board, number: int):
        self.board  = board
        self.number = number
