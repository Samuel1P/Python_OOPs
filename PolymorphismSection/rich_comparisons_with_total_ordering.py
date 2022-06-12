"""
Basic number class with rich comparison and total ordering from functools
Author: Samuel I P
"""
from __future__ import annotations
from functools import total_ordering

@total_ordering
class Number:
    """
    Basic Number class
    """
    def __init__(self, num) -> None:
        if not isinstance(num, int):
            return NotImplemented
        self.num = num
    
    def __eq__(self, other: Number) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return self.num == other.num
    
    def __gt__(self, other: Number) -> bool:
        if not isinstance(other, Number):
            return NotImplemented
        return self.num >  other.num

num1 = Number(1)
num2 = Number(2)
num3 = Number(3)
numone = Number(1)
numminusone = Number(-1)

"""
Before implimenting rich comparisons
print(num1 == num1) # True
print(num1 == num2) # False
print(num1 == numone) # False
print(num2 > num1) # TypeError: '>' not supported between instances of 'Number' and 'Number'
print(num2 >= num3) # TypeError: '>=' not supported between instances of 'Number' and 'Number' 
"""
# after implimenting rich comparisons
print(num1 == num1) # True
print(num1 == num2) # False
print(num1 == numone) # True
print(num2 > num1) # True
print(num2 > num3) # False

"""
without total ordering
print(num2 >= num3) # TypeError: '>=' not supported between instances of 'Number' and 'Number' 
"""
# with total ordering
print(num2 >= num3) # False
print(num2 <= num3) # True

