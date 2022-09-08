class Person:
    def __str__(self) -> str:
        print(f"String Person()")
        return self.__repr__()
    
    def __repr__(self) -> str:
        return f"Student()"
    
class Student(Person):
    def __repr__(self) -> str:
        return f"Student()"

obj1 = Person()
print(str(obj1))

obj2 = Student()
print(str(obj2))
