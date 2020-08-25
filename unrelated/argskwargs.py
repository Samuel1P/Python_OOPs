
def dyn_func(*args, **kwargs):
    print (*args)
    print (f" my name is {args}")
    print (kwargs)


dyn_func("sam","ip",s='b')