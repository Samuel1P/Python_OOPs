"""
Basic two dimensional vector rich comparisons
Author: Samuel I P
"""
from __future__ import annotations
from numbers import Real
from math import sqrt


class Vector:
    """
    A vector with x and y co-ordinate value
    """
    def __init__(self, *components: tuple[Real]) -> None:
        """
        init method that takes in x and y value as an unpacked iterable.
        """
        Vector.validate_input_vector(components)
        self.components = tuple(components)
        self.x = self.components[0]
        self.y = self.components[1]
    
    @staticmethod
    def validate_input_vector(co_ordinates_input: tuple[Real]) -> None:
        """
        Checks the input co-ordinates
        Args:
            co_ordinates_input (list): the input of x and y
        Raises:
            ValueError: Wrong co-ordinate length
            TypeError: Wrong co-ordinate type
        Returns:
            None
        """
        if len(co_ordinates_input) != 2:
            raise ValueError(f"Wrong co-ordinate length. Actual: {len(co_ordinates_input)}, Expected: 2")
        for location in co_ordinates_input:
            if not isinstance(location, Real):
                raise TypeError(f"Wrong co-ordinate type.  Actual: {type(location).__name__}, Expected: Real (int)")
        return
            
    def __repr__(self) -> str:
        """
        To view string representation of self
        Returns:
            str: string representation of self instance.
        """
        return f"Vector{self.components}"
    
    def __neg__(self) -> Vector:
        neg_vector = (-i for i in self.components)
        return Vector(*neg_vector)
    
    def __abs__(self) -> float:
        print(f"Absolute ->  {sum(i**2 for i in self.components)}")
        return float(f"{sqrt(sum(i**2 for i in self.components)):.2f}")
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __gt__(self, other) -> bool:
        if isinstance(other, Vector):
            return abs(self) > abs(other)
        return False
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Vector):
            return abs(self) < abs(other)
        return False
    
    def __le__(self, other) -> bool:
        if isinstance(other, Vector):
            return abs(self) < abs(other) or abs(self) == abs(other)
        return False
    
    
loc1 = Vector(2, 4)
print(loc1) # Vector(2, 4)
loc2 = Vector(5, 10)
print(loc2) # Vector(5, 10)

loc3 = Vector(10, 5)
print(loc3) # Vector(10, 5)

loc4 = Vector(-10, -5)
print(loc4) # Vector(-10, -5)

# absolute value - distance from origin
print(abs(loc1)) # 4.47
print(abs(loc2)) # 11.18
print(abs(loc3)) # 11.18
print(abs(loc4)) # 11.18



print(loc4 < loc1) # False
print(loc4 > loc3) # False
print(loc3 > loc4) # False
print(loc4 == loc3) # False


loc5 = Vector(-10, -5)
print(loc5) # Vector(-10, -5)


print(loc4 == loc5) # True
