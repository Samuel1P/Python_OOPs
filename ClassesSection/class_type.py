from types import FunctionType
class Person:
    pass

def func():
    pass

obj = Person()
print (type(Person))
print (Person)

print (type(Person()))
print (Person())
print(type(obj))
print(obj.__class__)
print(Person.__name__)
print (type(str))
print (type(func))
print (isinstance(func, FunctionType))
"""
<class 'type'>
<class '__main__.Person'>
<class '__main__.Person'>
<class '__main__.Person'>
Person
<class 'type'>
<class 'function'>
True
"""