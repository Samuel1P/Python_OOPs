

class Person:
    __slots__ = "_name", "__dict__"
    def __init__(self, name, age):
        self._name = name
        self.age = age
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        return self._name
    
Raj = Person("Raj", 26)

print(Raj.name)
print(Raj.age)
print(Raj.__dict__)