"""
Project Solution for Polymorphism
Author: Samuel I P
"""

from __future__ import annotations
from functools import total_ordering
from time import sleep

@total_ordering
class Mod:
    """
    Modulus class
    """
    def __init__(self, n_value: int, mod_value: int) -> None:
        """
        Constructor  
        Args:
            n_value (int): value of n
            mod_value (int): value of mod

        Raises:
            TypeError: if input_value is not of integer type.
        """
        if not isinstance(n_value, int):
            raise TypeError(f"Expects type int for value. Actual type is {type(n_value)} ({n_value})")
        if not isinstance(mod_value, int):
            raise TypeError(f"Expects type int for modulus. Actual type is {type(mod_value)} ({mod_value})")
        if mod_value <= 0:
            raise ArithmeticError(f"Expects postitive integers for modulus. Actual {mod_value}")
        self.n_value = n_value
        self._mod_value = mod_value
        self._value = self.n_value % self._mod_value
    
    @property
    def value(self) -> int:
        """
        value property
        Returns:
            int: value 
        """
        return self._value
    
    @property
    def mod_value(self) -> int:
        """
        mod property
        Returns:
            int: value of m
        """
        return self._mod_value
    
    def __hash__(self) -> int:
        """
        Generate hash based on self.value
        Returns:
            int: hash value
        """
        return hash((self.value, self.mod_value))
    
    def __int__(self) -> int:
        """
        Integer representation of Mod class
        Returns:
            int: int value
        """
        return int(self.value)
        
    def __str__(self) -> str:
        """
        Mod string representation for readability
        
        Returns:
            str: instance representation.
        """
        return f"Mod({self.n_value}, {self._mod_value}) ---> Mod({self._value}, {self._mod_value})"
    
    def __repr__(self) -> str:
        """
        Mod self representation
        
        Returns:
            str: instance representation.
        """
        return f"Mod({self._value}, {self._mod_value})"
    
    
    def __eq__(self, other: int|Mod) -> bool:
        """
        Equality Check for mods and ints
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: Raise if second operand is not int or Mod
        Returns:
            bool: True or False
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        return self.value == other_mod.value
    
    def __gt__(self, other: int|Mod) -> bool:
        """
        Greater than Check for mods and ints
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: Raise if second operand is not int or Mod
        Returns:
            bool: True or False
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        return self.value > other_mod.value
    
    
    def __add__(self, other: int|Mod) -> Mod:
        """
        Addition of two mods or mod and int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: summed mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        print("doing __add__")
        return Mod(self.value + other_mod.value, self.mod_value)
        
    def __sub__(self, other: int|Mod) -> Mod:
        """
        Substraction of two mods or mod and int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: substracted mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        return Mod(self.value - other_mod.value, self.mod_value)

        
    def __mul__(self, other: int|Mod) -> Mod:
        """
        Multiplication of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: multiplied mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        return Mod(self.value * other_mod.value, self.mod_value)

    def __pow__(self, other: int|Mod) -> Mod:
        """
        exponential of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: multiplied mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        return Mod(self.value ** other_mod.value, self.mod_value)
    
    def __iadd__(self, other: int|Mod) -> Mod:
        """
        in place addition of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: summed mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        self._value = self.value + other_mod.value
        return self
    
    def __isub__(self, other: int|Mod) -> Mod:
        """
        In place subsctration of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: summed mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        self._value = self.value - other_mod.value
        return self
    
    
    def __imul__(self, other: int|Mod) -> Mod:
        """
        In place Multiplication of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: multiplied mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        self._value = (self.value * other_mod.value) % self.mod_value
        return self

    def __ipow__(self, other: int|Mod) -> Mod:
        """
        in-place exponential of two mods or mod and an int
        Args:
            other (int | Mod): second operand
        Raises:
            TypeError: if second operand is not int or Mod
            ArithmeticError: if second operand is of different mod
        Returns:
            Mod: multiplied mod
        """
        other_mod = self.type_check(other)
        self.mod_check(other_mod)
        self._value = (self.value ** other_mod.value ) % self.mod_value
        return self
    
    def mod_check(self, operand):
        """
        Modulus check of input operand with self
        Args:
            operand (Mod): other operand
        Raises:
            ArithmeticError: Different modulus to self
        """
        if operand.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {operand.mod_value}")
        return True

    def type_check(self, operand):
        """
        Check if the operand is int or mod
        Args:
            input_data (int|Mod): other operand
        Raises:
            TypeError: Wrong type
        """
        if isinstance(operand, int):
            other_mod = Mod(operand, self.mod_value)
        elif isinstance(operand, Mod):
            other_mod = operand
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(operand)} ({operand})")
        return other_mod


A = Mod(10,12)
B = Mod(22,12)
C = 3
D = 10
E = Mod(142,12)
"""
print(repr(A)) # Mod(10, 12)
print(repr(C)) # 3


print(A==C) # False
print(A>C) # True
print(A==B) # True
print(A>=D) # True

print(hash(E)) # 10
print(int(E)) # 10
print(repr(A+B)) # Mod(8, 12)
"""
print("==")

A = Mod(9,12)
print(A, A.value, A.mod_value, id(A))

A += 1
print(A, A.value, A.mod_value, id(A))  # Mod(9, 12)
print("==")


A = Mod(9,12)
print(A, A.value, A.mod_value, id(A))

A = A + 1
print(A, A.value, A.mod_value, id(A))  # Mod(9, 12)
print("==")

"""
A * C # Mod(0, 12)
print(A, A.value, A.mod_value)
A = Mod(10,12)
A*=C
print(A, A.value, A.mod_value)
"""