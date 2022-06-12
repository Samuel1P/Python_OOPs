class FunctionMethods:
    def hello():
        print ("hello..from ...plain hello")
        
    def instance_hello(self):
        print (f"hello..from {self} ...instance hello")
    
    @classmethod    
    def class_hello(cls):
        print (f"hello..from  ...class hello")
    
    @staticmethod
    def static_hello():
        print ("hello..from ...static hello")
    
obj = FunctionMethods()
print (100*"=")

#calling a method inside class- python does not inject any arg
#<function FunctionMethods.hello at 0x10fee1e50>
#hello..from ...plain hello
print (FunctionMethods.hello)
FunctionMethods.hello()
print (100*"*")

#calling a method inside class using instance reference 
# python will try to inject instance as first arg, but method does not expect it, so it will FAIL
# <bound method FunctionMethods.hello of <__main__.FunctionMethods object at 0x107fb5f70>>
# hello() takes 0 positional arguments but 1 was given
try:
    print (obj.hello)
    obj.hello()
except Exception as exe:
    print (exe)

print (100*"*")

#call an instance function, it becomes bound to the instance object
# python injects instance as first arg
#<bound method FunctionMethods.instance_hello of <__main__.FunctionMethods object at 0x10e047f70>>
#hello..from <__main__.FunctionMethods object at 0x10e047f70> ...instance hello
print (obj.instance_hello)
obj.instance_hello()
print (100*"*")

# call instance function using class reg
# this will fail because python will not inject object
# but instance method expects an instance object
# <function FunctionMethods.instance_hello at 0x108075ee0>
# instance_hello() missing 1 required positional argument: 'self'
try:
    print (FunctionMethods.instance_hello)
    FunctionMethods.instance_hello()
except TypeError as exc:
    print (exc)
print (100*"*")

# calling class method - python injects class object
# the function becomes bound method to class
# <bound method FunctionMethods.class_hello of <class '__main__.FunctionMethods'>>
# hello..from  ...class hello
print (FunctionMethods.class_hello)
FunctionMethods.class_hello()
print (100*"*")

# eventhough instance object is injected, the class method only gets bound to class
# <bound method FunctionMethods.class_hello of <class '__main__.FunctionMethods'>>
# hello..from  ...class hello
print (obj.class_hello)
obj.class_hello()
print (100*"*")

# static method, python does not inject class nor instance
# method does not get bound to class nor instance
# <function FunctionMethods.static_hello at 0x10d8ea040>
# hello..from ...static hello
print (obj.static_hello)
obj.static_hello()
print (100*"*")

# static method, python does not inject class nor instance
# method does not get bound to class nor instance
# <function FunctionMethods.static_hello at 0x10d8ea040>
# hello..from ...static hello
print (obj.static_hello)
obj.static_hello()
print (100*"=")
