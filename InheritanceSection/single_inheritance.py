class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass

print()
print(f"issubclass(Ellipse, Shape) --> {issubclass(Ellipse, Shape)}")
print(f"issubclass(Circle, Ellipse) --> {issubclass(Circle, Ellipse)}")
print(f"issubclass(Circle, Shape) --> {issubclass(Circle, Shape)}")

sh = Shape()
sq = Square()
rt = Rectangle()


print()
print(f"isinstance(sh, Shape) --> {isinstance(sh, Shape)}")
print(f"isinstance(sq, Square) --> {isinstance(sq, Square)}")
print(f"isinstance(sq, Square) --> {isinstance(sq, Shape)}")

print()
cr = Circle()
el = Ellipse()
print(f"type(Ellipse) -> {type(Ellipse)}")
print(f"type(el) -> {type(el)}")
print()
print(f"isinstance(cr, type(el)) -> {isinstance(cr, type(el))}")
print(f"issubclass(type(cr), type(el)) -> {issubclass(type(cr), type(el))}")

"""
Output:

issubclass(Ellipse, Shape) --> True
issubclass(Circle, Ellipse) --> True
issubclass(Circle, Shape) --> True

isinstance(sh, Shape) --> True
isinstance(sq, Square) --> True
isinstance(sq, Square) --> True

type(Ellipse) -> <class 'type'>
type(el) -> <class '__main__.Ellipse'>

isinstance(cr, type(el)) -> True
issubclass(type(cr), type(el)) -> True
"""