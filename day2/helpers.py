from enum import Enum

class Base:
    __slots__ = ()

    def __str__(self):
        return ', '.join(f'{x} => {getattr(self, x)}' for x in self.__slots__)

    def __repr__(self):
        return str(self)

class Command(Base):
    class Direction(Enum):
        down    = 1
        forward = 2
        up      = 3

    __slots__ = ('direction', 'amount')

    def __init__(self, direction: Direction, amount: int):
        self.direction = direction
        self.amount    = amount

    @classmethod
    def from_raw(cls, raw) -> 'Command':
        direction, amount = raw.split()
        return cls(cls.Direction[direction], int(amount))

class Position(Base):
    __slots__ = ('depth', 'horizontal', 'aim')

    def __init__(self, depth: int = 0, horizontal: int = 0, aim: int = 0):
        self.depth      = depth
        self.horizontal = horizontal
        self.aim        = aim
