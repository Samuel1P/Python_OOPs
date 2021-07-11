class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

ind_time = Time(23, 13)
us_time = Time(1,25)
print (ind_time.__dict__)

def say_time(self):
    print (f"Time here is {self.hour}:{self.min}.")


print (ind_time.__dict__)

from types import MethodType
my_bound = MethodType(say_time, ind_time)
setattr(ind_time, "say_time", my_bound)
print (ind_time.__dict__)

ind_time.say_time()