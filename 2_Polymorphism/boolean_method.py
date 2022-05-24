"""
Defining custom booleans.

If bool is not defined, python looks for length of the object and returns the boolean of its value. If Length is also not defined, it simple returns True.
"""

class Vector:
    """
    A vector with x and y co-ordinate value
    """
    def __init__(self, x, y) -> None:
        """
        init method that takes in x and y value as an unpacked iterable.
        """
        self.x = x
        self.y = y
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    
loc1 = Vector(0,0)
loc2 = Vector(0,1)

print(bool(loc1), bool(loc2)) # False True


