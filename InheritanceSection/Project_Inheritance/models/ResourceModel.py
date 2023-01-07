


class Resource:
    """
    Basic resource class that is used in PC builds 
    """
    def __init__(self, name, manufacturer, total, allocated) -> None:
        """
        Init for any item in PC builds.
        Args:
            name (str): Name of the item
            manufacturer (str): Vendor name
            total (int): total number of items
            allocated (int): items in use
        """
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated
    
    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def total(self):
        return self._total
    
    @property
    def allocated(self):
        return self._allocated
    
    def claim(self, n):
        if n > self.total:
            return False
        self._total -= n
        self._allocated += n
        return True
    
    def purchase(self, n):
        self._total += n
        return True
    
    def died(self, n):
        self._allocated -= n
        self._total -= n
        return True