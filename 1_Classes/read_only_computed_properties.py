from math import pi

class Circle():
    def __init__(self, rad) -> None:
        self._radius = rad
    
    # radius = property(fget = radius)
    @property
    def radius(self):
        return self._radius
    
    # radius = radius(fset = radius)
    # property_obj = exisiting property object with getter ( adding a setter property mehtod)
    @radius.setter
    def radius(self, value):
        self._radius = value

    # area = property(fget=area)
    @property
    def area(self):
        print (f"calculating radius for... {self.radius}.")
        import time
        time.sleep(3) 
        return pi * (self.radius ** 2)

ball = Circle(5)
print (ball.radius)
print (ball.area)
ball.radius = 2
print (ball.radius)
print (ball.area)
print (ball.area)
print (ball.area)
print (ball.area)