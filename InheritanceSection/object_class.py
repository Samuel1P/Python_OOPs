
class Person:
    pass

print(dir(object))
"""
Output:

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""

p = Person()
print(id(Person.__init__), id(object.__init__)) # both are same

# Anything of type type (Class), inherits from the object class by default.