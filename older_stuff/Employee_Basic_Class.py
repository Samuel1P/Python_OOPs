
class Employee:
    def __init__(self, fname, lname, age):
        self.fname_ = fname
        self.lname_ = lname
        self.age = age

    @classmethod
    def ord_method(cls):
        return ("Method without self")

    def basic_details(self):
        return f"{self.fname_} {self.lname_} is {self.age} years old."


Emp1 = Employee("Tom","Day",25)
Emp2 = Employee("Robert","Ford",42)

#print (Emp1.basic_details())
#print (Emp2.basic_details())

print (Employee.ord_method())