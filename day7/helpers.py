class Base:
    __slots__ = ()

    def __str__(self):
        return ', '.join(f'{x} => {getattr(self, x)}' for x in self.__slots__)

    def __repr__(self):
        return str(self)

class SearchResult(Base):
    __slots__ = ('start', 'end', 'cost')

    def __init__(self, start: int, end: int, cost: int):
        self.start = start
        self.end   = end
        self.cost  = cost

    def __eq__(self, other: 'SearchResult') -> bool:
        return self.start == other.start and self.end == other.end and self.cost == other.cost


"""Failed logic: Tried to do a kind of binary search to find the lowest fuel but it didn't work."""
# def decide_start_end(last_result: SearchResult) -> SearchResult:
#     half = (last_result.start + last_result.end) // 2
#     cost = get_fuel_cost((last_result.start + half) // 2)
#     if cost < last_result.cost:
#         result = SearchResult(last_result.start, half, cost)
#     else:
#         result = SearchResult(half, last_result.end, cost)
#     print(result)
#     return result

# found       = False
# last_result = SearchResult(0, max(positions), get_fuel_cost((max(positions)//2)))
# while not found:
#     result      = decide_start_end(last_result)
#     found       = last_result == result
#     last_result = result

# print(last_result)

# 351901 is correct, index 342