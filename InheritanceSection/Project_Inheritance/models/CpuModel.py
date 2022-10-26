from ResourceModel import Resource
#from InheritanceSection.Project_Inheritance.models.ResourceModel import Resource


class Cpu(Resource):
    def __init__(self, name, manufacturer, total, cores, sockets, power) -> None:
        self._cores = cores
        self._sockets = sockets
        self._power = power
        super().__init__(name, manufacturer, total)


#

Cpu1 = Cpu("i3 Pentium", "Intel", 5, 2, 4, 20)
print(Cpu1.__dict__)
print(Cpu1.claim(3))
print(Cpu1.__dict__)
print(Cpu1.purchase(10))
print(Cpu1.__dict__)


