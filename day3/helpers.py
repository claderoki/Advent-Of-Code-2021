class Base:
    __slots__ = ()

    def __str__(self):
        return ', '.join(f'{x} => {getattr(self, x)}' for x in self.__slots__)

    def __repr__(self):
        return str(self)

class Report(Base):
    __slots__ = ('gamma_rate', 'epsilon_rate')

    def __init__(self, gamma_rate: int, epsilon_rate: int):
        self.gamma_rate   = gamma_rate
        self.epsilon_rate = epsilon_rate

