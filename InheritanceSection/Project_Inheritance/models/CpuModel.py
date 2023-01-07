from ResourceModel import Resource
#from InheritanceSection.Project_Inheritance.models.ResourceModel import Resource


class CPU(Resource):
    def __init__(self, name, manufacturer, total, cores, sockets, power) -> None:
        super().__init__(name, manufacturer, total)
        self._cores = cores
        self._sockets = sockets
        self._power = power
