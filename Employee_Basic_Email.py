
class Employee:
    def __init__(self, fname, lname, age):
        self.fname_ = fname
        self.lname_ = lname
        self.age = age

    def basic_details(self):
        return f"{self.fname_} {self.lname_} is {self.age} years old."

    def get_email(self):
        return f"{self.fname_}{self.lname_}@email.com"

Emp1 = Employee("Tom","Day",25)
Emp2 = Employee("Robert","Ford",42)

print (Emp1.basic_details())
print (Emp2.basic_details())
print (Emp1.get_email())
print (Emp2.get_email())