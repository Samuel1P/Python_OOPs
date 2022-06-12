class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def execute(self, bound_runtime_funx):
        from types import MethodType
        bound_meth = MethodType(bound_runtime_funx, self)
        setattr(self, "task", bound_meth)

    @property
    def specific_task(self):
        self.task = getattr(self, "task", None )
        if self.task:
            return self.task()
        return NotImplementedError

ind_time = Time(23, 13)
us_time = Time(1,25)
print (ind_time.__dict__)
th = lambda self: f"Time here is {self.hour}:{self.min}"

ind_time.execute(th)

print (ind_time.__dict__)

print (ind_time.specific_task)