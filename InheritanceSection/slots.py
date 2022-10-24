

class Location:
    __slots__ = "name", "_latitude", "_longitude" # has to be a iterable
    def __init__(self, name, latitude, longitude):
        self.name = name
        self._latitude = latitude
        self._longitude = longitude
        
    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude


print(Location.__dict__)
Location.provider = "Google"
print(Location.__dict__)


Madurai = Location("Madurai", latitude=9.9, longitude=78.1)

