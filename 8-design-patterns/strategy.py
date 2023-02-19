# Open-Closed Principle; Open for extensions, but closed for modification
# Strategy pattern

# example filter an array by removing all positive or odd values

from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def removeValue(self, val):
        return val < 0

class RemoveOddStrategy(FilterStrategy):

    def removeValue(self, val):
        return abs(val) % 2
    

class Values:
    def __init__(self, vals) -> None:
        self.vals = vals

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
# test

values = Values([-7, -4, -1, 0, 2, 6, 9])

# this allows the ability to add different strategies without 
# modifying the values class
print(values.filter(RemoveNegativeStrategy())) # [0, 2, 6, 9]
print(values.filter(RemoveOddStrategy())) # [-4, 0, 2, 6]