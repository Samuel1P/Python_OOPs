class Person:
    name = "Unknown"
    def __init__(self):
        print ("dunder init...")

    @classmethod
    def normal(cls):
        pass
    def name_only(self):
        print ("this is a bound meth")

print (Person.__dict__)
obj = Person()
print (obj.__dict__)

obj.lamb_func = lambda : "this is a lambda func"
print (obj.__dict__)
print (obj.name_only)
print (obj.__dict__)
print (Person.name_only)