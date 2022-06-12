"""
Implimenting __del__ is fruitless since Pythons GC is not going to delete
the object from memory unless all the reference are deleted. The problem here
is identifying all the references of the object. For example, when an 
exception is raised and exception object is stored, it holds on to a ref to
the object internally [[<exception_obj.__traceback__.tb_frame.f_locals.copy().items()>
Looks for instance of the object in values]]. Also any exceptions in __del__ getd silenced
and sent to sys.std.err.
"""


import ctypes 

def count_ref(obj_address):
    return ctypes.c_long.from_address(obj_address).value

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __del__(self):
        print("__del__ called...")

p = Person("Shawn")
address = id(p)
print(address, count_ref(id(address)))
del p

print(address, count_ref(id(address)))
