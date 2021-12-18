class Base:
    __slots__ = ()

    def __str__(self):
        return ', '.join(f'{x} => {getattr(self, x)}' for x in self.__slots__)

    def __repr__(self):
        return str(self)

class Cell(Base):
    __slots__ = ('count', )

    def __init__(self):
        self.count = 0

    def __str__(self) -> str:
        return str(self.count) if self.count > 0 else '.'

class Position(Base):
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
