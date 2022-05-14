"""
Basic two dimensional vector calculation
Author: Samuel I P
"""
from __future__ import annotations
from numbers import Real

class Vector:
    """
    A vector with x and y co-ordinate value
    """
    def __init__(self, *components) -> None:
        Vector.validate_input_vector(components)
        self.components = tuple(components)
    
    @staticmethod
    def validate_input_vector(co_ordinates_input: list) -> None:
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
                raise TypeError(f"Wrong co-ordinate type.  Actual: {type(location).__name__}, Expected: int")
        return
            
    def __repr__(self) -> str:
        """
        To view string representation of self
        Returns:
            str: string representation of self instance.
        """
        return f"Vector{self.components}"

    def __add__(self, other_vector: Vector) -> Vector:
        """Adds two vectors
        Args:
            other_vector (Vector): the second vector as arg
        Returns:
            Vector: sum of both vectors
        """
        sum_vector = (x + y for x, y in zip(self.components, other_vector.components))
        return Vector(*sum_vector)
    
    
loc1 = Vector(2, 4)
print(loc1) # Vector(2, 4)
loc2 = Vector(5, 10)
print(loc2) # Vector(5, 10)
loc3 = loc1 + loc2
print(loc3) # Vector(7, 14)

# exceptions
# loc4 = Vector("2", 5) # TypeError: Wrong co-ordinate type.  Actual: str, Expected: int
# loc4 = Vector(2, 5, 10) # ValueError: Wrong co-ordinate length. Actual: 3, Expected: 2