"""
Implementing custom format is complex and goes outside the scope of OOP.
We will reuse the existing formatting spec of the objects to get around.
"""


from datetime import date

class Person:
    def __init__(self, name, dob) -> None:
        self.name = name
        self.dob = dob
    
    def __repr__(self):
        return f"Person({self.name}, {self.dob})"
    
    def __format__(self, format_spec):
        return f"{self.name}:{format(self.dob, format_spec)}"
    

p = Person("Pat", date(1993, 10, 1))

print(p) # Person(Pat, 1993-10-01)
print(format(p, f" %A, %d-%B-%Y")) # Pat: Friday, 01-October-1993