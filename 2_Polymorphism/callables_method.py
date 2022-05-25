"""
Creating callable methods to class instances : Default Dict
"""

from collections import defaultdict

class default_value:
    def __init__(self, value):
        self.value = value
        self.counter = 0
    
    def __call__(self, *args, **kwds):
        self.counter += 1
        return self.value
    
    

NA = default_value("N/A")
NONE = default_value(None)
MISSING = default_value("MISSING")

dict1 = defaultdict(NA)
dict2 = defaultdict(NONE)
dict3 = defaultdict(MISSING)
dict4 = defaultdict(list)

print(dict1['a']) # N/A
print(dict2['a']) # None
print(dict3['a']) # MISSING
print(dict4['a']) # []

print(NA.counter) # 1
print(dict1['b']) # N/A
print(dict1['c']) # N/A

print(NA.counter) # 3
