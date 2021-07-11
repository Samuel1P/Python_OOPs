class Laptop:
    GPU = "AMD"
    storage = "3 TB"
    _release = 2020
    cores = 8


print (Laptop.__dict__)
setattr(Laptop, "RAM", "8 GB")
print (Laptop.__dict__)
dis = getattr(Laptop, "display_size", "Display size not available") #throws attribute error without that last arg
print (f"Display size: {dis}")
Laptop.display_size = "15.6 inches"
dis = getattr(Laptop, "display_size", "Display size not available")
print (f"Display size: {dis}")
delattr(Laptop, "cores")
core = getattr(Laptop, "cores","Core info is not available.")
print (core)
del Laptop.storage
print (Laptop.__dict__)

print(Laptop.__dict__.values())
