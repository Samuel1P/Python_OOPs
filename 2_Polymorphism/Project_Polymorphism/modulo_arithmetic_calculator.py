"""
Project Solution for Polymorphism
Author: Samuel I P
"""

from __future__ import annotations

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
            raise TypeError(f"Expects type int. Actual type is {type(n_value)} ({n_value})")
        if mod_value <= 0:
            raise ArithmeticError(f"Expects postitive integers. Actual {mod_value}")
        self.n_value = n_value
        self._mod_value = mod_value
        self._value = self.calculate_modulo(self.n_value, self._mod_value)
    
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
        return hash(self.value)
    
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
    
    def calculate_modulo(self, value: int, mod: int) -> Mod:
        return value % mod
    
    
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
        if isinstance(other, int):
            other_mod = Mod(other, self.mod_value)
        elif isinstance(other, Mod):
            other_mod = other
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(other)} ({other})")
        if other_mod.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {other_mod.mod_value}")
        return self.value == other_mod.value
    
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
        if isinstance(other, int):
            other_mod = Mod(other, self.mod_value)
        elif isinstance(other, Mod):
            other_mod = other
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(other)} ({other})")
        if other_mod.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {other_mod.mod_value}")
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
        if isinstance(other, int):
            other_mod = Mod(other, self.mod_value)
        elif isinstance(other, Mod):
            other_mod = other
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(other)} ({other})")
        if other_mod.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {other_mod.mod_value}")
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
        if isinstance(other, int):
            other_mod = Mod(other, self.mod_value)
        elif isinstance(other, Mod):
            other_mod = other
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(other)} ({other})")
        if other_mod.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {other_mod.mod_value}")
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
        if isinstance(other, int):
            other_mod = Mod(other, self.mod_value)
        elif isinstance(other, Mod):
            other_mod = other
        else:
            raise TypeError(f"Expects type int or Mod. Actual type is {type(other)} ({other})")
        if other_mod.mod_value != self.mod_value:
            raise ArithmeticError(f"Cannot compare operands with different modulus. Actual: {self.mod_value} and {other_mod.mod_value}")
        return Mod(self.value ** other_mod.value, self.mod_value)
    
    
A = Mod(10,12)
B = Mod(22,12)
C = 3

print(repr(A))
print(repr(B))
print(A==C)
print(A==B)

print(hash(A))
print(int(A))
print(repr(A+B))