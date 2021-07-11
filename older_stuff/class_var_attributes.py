def called_class():
    print ("Class assignment")
    return 2

class Bar(object):
    y = called_class()
    def __init__(self, x):
        self.x = x

def called_instance():
    print ("Instance assignment")
    return 2

class Foo(object):
    def __init__(self, x):
        self.y = called_instance()
        self.x = x

Bar(1)
print (Bar.__dict__)
print (25*"-")
Bar(2)
print (Bar.__dict__)
print (25*"-")
Foo(1)
print (Bar.__dict__)
print (25*"-")
Foo(2)
print (Bar.__dict__)