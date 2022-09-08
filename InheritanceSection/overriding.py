class Person:
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def whoami(self):
        print("I am a Person")
    
    def my_species(self):
        print("I am of species homo sapiens")
    
    def my_role(self):
        return self.whoami()
    
class Student(Person):
    def whoami(self):
        print("I am a Student")

obj1 = Person()
print(str(obj1))

obj2 = Student()

obj2.whoami() # I am a Student
obj2.my_species() # I am of species homo sapiens
obj2.my_role() # I am a Student