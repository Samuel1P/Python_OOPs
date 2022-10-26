


class Resource:
    def __init__(self, name, manufacturer, total) -> None:
        self.name = name
        self.manufacturer = manufacturer
        self.total = total
        self.allocated = int()
    
    def claim(self, n):
        if n > self.total:
            return False
        self.total -= n
        self.allocated += n
        return True
    
    def purchase(self, n):
        self.total += n
        return True