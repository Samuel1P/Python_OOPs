
def out_func(arg):

    x = "some value"
    def inner_func():
        print (x, arg)
    return inner_func

close_obj = out_func("::some arg::")
close_obj2 = out_func("::same arg::")
close_obj3 = out_func("::sometime arg::")

close_obj()
close_obj2()
close_obj3()
