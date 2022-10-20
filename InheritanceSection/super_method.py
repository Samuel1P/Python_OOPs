
import re


class Human:
    def live(self):
        return f"...In '{self.__class__.__name__}' class, Human lives ..."


class Student(Human):
    def study(self):
        return f"...In '{self.__class__.__name__}' class, Student studies ..."
    
class ComputerStudent(Student):
    def codes(self):
        out = f"...In '{self.__class__.__name__}' class, Computer Student lives ..."
        out += super().study()
        out += super().live()
        return out

    def live():
        return "just die bro" # let's not do that, delegate this above
    
s1 = Student()
print(s1.live())

print("*"*70)

cs1 = ComputerStudent()
print(cs1.codes())
print("*"*70)