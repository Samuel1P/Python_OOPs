from functools import wraps
class Circle:
    def __init__(self, radius) -> None:
        self._radius = int(radius)
    
    def custom_property(func):
        print ("custom property..")
        def inner(*args):
            print ("inner property..")
            print (func(args[0]))
            return func(args[0])
        print ("outer property..")
        return inner

    @custom_property
    def area2(self):
        print ("Area 2")
        print (6.14 * self._radius)
        return 6.14 * self._radius

# c1 = Circle(2)
# c1.area2()

def custom_property(func):
    print ("222custom property..")
    def inner():
        print ("222inner property..")
        print (func())
        return func()
    print ("222outer property..")
    return inner()

@custom_property
def area2():
    print ("Area 222")
    print (6.14)
    return 6.14

