from math import pi

class Circle():
    def __init__(self, rad) -> None:
        self._radius = rad
        self._area = None
    
    # radius = property(fget = radius)
    @property
    def radius(self):
        return self._radius
    
    # radius = radius(fset = radius)
    # property_obj = exisiting property object with getter ( adding a setter property mehtod)
    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Radius is invalid.")
        print (f"setting new radius as {new_radius}")
        self._radius = new_radius
        self._area = None
        print ("cache cleared.")


    # area = property(fget=area)
    @property
    def area(self):
        if self._area is None:
            print ("doing area calculation....")
            self._area = pi * (self.radius ** 2)
        return self._area

ball = Circle(5)
print (ball.__dict__)
print (ball.radius)
print (ball.area)
ball.radius = 2
print (ball.radius)
print (ball.__dict__)
print (ball.area)
print (ball.area)
print (ball.__dict__)
print (ball.area)
print (ball.area)


"""
{'_radius': 5, '_area': None}
5
doing area calculation....
78.53981633974483
setting new radius as 2
cache cleared.
2
{'_radius': 2, '_area': None}
doing area calculation....
12.566370614359172
12.566370614359172
{'_radius': 2, '_area': 12.566370614359172}
12.566370614359172
12.566370614359172
"""