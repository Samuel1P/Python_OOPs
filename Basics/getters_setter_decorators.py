class Employee:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age


    @property
    def name(self):
        print("getting name..")
        return self._name

    @name.setter
    def name(self, name):
        print ("setting name...")
        self._name = name

    @name.deleter
    def name(self):
        print ("deleting name...")
        del self._name
    
    @property
    def age(self):
        print (self._age)
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


emp1 = Employee("Smith", 23)

emp1.name
emp1.age
emp1.name = "Nate"
emp1.age = 33
emp1.name
emp1.age
del emp1.name
emp1.age
try:
    emp1.name
except AttributeError as exe:
    print (f"AttributeError : {exe}")