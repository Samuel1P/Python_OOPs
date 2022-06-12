"""
Creating decorator out of a class using callable methods.
"""

from time import sleep, perf_counter
from random import randint


class time_profiler:
    def __init__(self, func):
        self.func = func
        self.run_count = 0
        self.total_time_run = 0
    
    @property
    def avg_time(self):
        return f"{(self.total_time_run / self.run_count):.2f}"
    
    def __call__(self, *args, **kwds):
        self.run_count += 1 
        start = perf_counter()
        run_return = self.func()
        end = perf_counter()
        self.total_time_run += end - start
        return run_return


@time_profiler
def some_operation():
    secs = randint(1,5)
    print(f"Starting operation that takes {secs:.2f} seconds.")
    sleep(secs)
    print("Operation completed")

# some_operation = time_profiler(some_operation)

some_operation()

print("Average execution time: ", some_operation.avg_time)
some_operation()
some_operation()
some_operation()
print("Average execution time: ", some_operation.avg_time)
print("Total runs so far : ",some_operation.run_count)