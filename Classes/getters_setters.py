from typing import Protocol


class Employee:
    def __init__(self, name) -> None:
        self._name = name
    
    def get_name(self):
        print ("Getting name..")
        if  hasattr(self, '_name'):
            print(self._name) 
        else:
            print("Name not found")

    def set_name(self, name):
        print ("Setting name..")
        if isinstance(name, str):
            self._name = name
        else:
            print("name is invalid")

    def del_name(self):
        print ("Deleting name..")
        if hasattr(self, '_name'):
             del self._name
        else:
            print ("name not found")


    name = property(fget=get_name, fset=set_name, fdel=del_name)

Emp1 = Employee("Tom")
Emp1.name
Emp1.name = "Brian"
del Emp1.name
Emp1.name
Emp1.name = "Jim"
Emp1.name