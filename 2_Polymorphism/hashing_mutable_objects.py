"""
Retaining hashing to class where we have custom equality implimented
"""

from __future__ import annotations


class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other: Person) -> bool:
        return self.name == other.name
    
    
Tom = Person("Tom")
Akbar = Person("Akbar")
Tom2 = Person("tom")
Tom3 = Person("Tom")

"""
# Before implimenting __eq__
print(Tom == Tom3) # False
print(Tom is Tom3) # False

# After implimenting __eq__ and Before implimenting hash
print(Tom == Tom3) # True
print(Tom is Tom3) # False
print(hash(Tom)) # TypeError: unhashable type: 'Person'
"""

# After implimenting both eq and hash
print(hash(Tom)) # 4337803216
print(hash(Akbar)) # 4337803120
print(hash(Tom2)) # 4337803024
print(hash(Tom3)) # 4337800384
print(Tom == Tom3) # True
print(Tom is Tom3) # False
print({Tom: "Tom1s class insance"}) # {<__main__.Person object at 0x10afdbfd0>: 'Tom1s class insance'}


"""
https://stackoverflow.com/a/34406010/13223901

There are three concepts to grasp when trying to understand id, hash and the == and is operators: identity, value and hash value. Not all objects have all three.

All objects have an identity, though even this can be a little slippery in some cases. The id function returns a number corresponding to an object's identity (in cpython, it returns the memory address of the object, but other interpreters may return something else). If two objects (that exist at the same time) have the same identity, they're actually two references to the same object. The is operator compares items by identity, a is b is equivalent to id(a) == id(b).

Identity can get a little confusing when you deal with objects that are cached somewhere in their implementation. For instance, the objects for small integers and strings in cpython are not remade each time they're used. Instead, existing objects are returned any time they're needed. You should not rely on this in your code though, because it's an implementation detail of cpython (other interpreters may do it differently or not at all).

All objects also have a value, though this is a bit more complicated. Some objects do not have a meaningful value other than their identity (so value an identity may be synonymous, in some cases). Value can be defined as what the == operator compares, so any time a == b, you can say that a and b have the same value. Container objects (like lists) have a value that is defined by their contents, while some other kinds of objects will have values based on their attributes. Objects of different types can sometimes have the same values, as with numbers: 0 == 0.0 == 0j == decimal.Decimal("0") == fractions.Fraction(0) == False (yep, bools are numbers in Python, for historic reasons).

If a class doesn't define an __eq__ method (to implement the == operator), it will inherit the default version from object and its instances will be compared solely by their identities. This is appropriate when otherwise identical instances may have important semantic differences. For instance, two different sockets connected to the same port of the same host need to be treated differently if one is fetching an HTML webpage and the other is getting an image linked from that page, so they don't have the same value.

In addition to a value, some objects have a hash value, which means they can be used as dictionary keys (and stored in sets). The function hash(a) returns the object a's hash value, a number based on the object's value. The hash of an object must remain the same for the lifetime of the object, so it only makes sense for an object to be hashable if its value is immutable (either because it's based on the object's identity, or because it's based on contents of the object that are themselves immutable).

Multiple different objects may have the same hash value, though well designed hash functions will avoid this as much as possible. Storing objects with the same hash in a dictionary is much less efficient than storing objects with distinct hashes (each hash collision requires more work). Objects are hashable by default (since their default value is their identity, which is immutable). If you write an __eq__ method in a custom class, Python will disable this default hash implementation, since your __eq__ function will define a new meaning of value for its instances. You'll need to write a __hash__ method as well, if you want your class to still be hashable. If you inherit from a hashable class but don't want to be hashable yourself, you can set __hash__ = None in the class body.


"""