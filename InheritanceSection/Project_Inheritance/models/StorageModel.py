from ResourceModel import Resource

class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb) -> None:
        super().__init__(name, manufacturer, total, allocated)
        self._capacity_GB = capacity_gb

    @property
    def capacity_gb(self):
        return self.capacity_gb

class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface
    
    @property
    def interface(self):
        return self._interface

class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm, ) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._size = size
        self._rpm = rpm
    
    @property
    def size(self):
        return self._size
    
    @property
    def rpm(self):
        return self._rpm