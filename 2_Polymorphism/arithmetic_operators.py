"""
Basic two dimensional vector calculation
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

    def __add__(self, other_vector: Vector) -> Vector:
        """
        Adds two vectors
        Args:
            other_vector (Vector): the second vector as arg
        Returns:
            Vector: sum of both vectors
        """
        sum_vector = (x + y for x, y in zip(self.components, other_vector.components))
        return Vector(*sum_vector)
    
    def __sub__(self, other_vector: Vector) -> Vector:
        """
        Substracts two vectors
        Args:
            other_vector (Vector): the second vector as arg
        Returns:
            Vector: sum of both vectors
        """
        sum_vector = (x - y for x, y in zip(self.components, other_vector.components))
        return Vector(*sum_vector)

    def __mul__(self, other: Real | Vector) -> Vector | Real:
        """
        Multiply vectors with vectors and numbers
        Args:
            other (Real | Vector): a vector or integer 
        Returns:
            Vector | Real: a result vector or integer 
        """
        if isinstance(other, Real):
            mul_vector = (item * other for item in self.components)
            return Vector(*mul_vector)
        if isinstance(other, Vector):
            mul_values = (x * y for x, y in zip(self.components, other.components))
            return sum(mul_values)
        return NotImplemented
    
    def __rmul__(self, other: Real) -> Vector:
        """
        To multiply number and vector (reflective mul)
        Args:
            other (Real): The number
        Returns:
            Vector: result vector
        """
        return self * other 
    
    def __neg__(self) -> Vector:
        neg_vector = (-i for i in self.components)
        return Vector(*neg_vector)
    
    def __abs__(self) -> int:
        return sqrt(sum(i**2 for i in self.components))


loc1 = Vector(2, 4)
print(loc1) # Vector(2, 4)
loc2 = Vector(5, 10)
print(loc2) # Vector(5, 10)

# add
loc3 = loc1 + loc2
print(loc3) # Vector(7, 14)

# substract
loc4 = loc3 - loc3
print(loc4) # Vector(0, 0)

# multiply
loc5 = loc1 * 2
print(loc5) # Vector(4, 8)
loc6 = 2 * loc1
print(loc6) # Vector(4, 8)

# dot product - (2, 4) & (5, 10)
# (2 * 5) + (4 * 10); 10 + 40; 50
value = loc1 * loc2
print(value) # 50

print(loc4 < loc5)
# to do
# iadd, neg and abs

# exceptions
# loc4 = Vector("2", 5) # TypeError: Wrong co-ordinate type.  Actual: str, Expected: int
# loc4 = Vector(2, 5, 10) # ValueError: Wrong co-ordinate length. Actual: 3, Expected: 
# 
