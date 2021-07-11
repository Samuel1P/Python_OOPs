class mobile:
    def __init__(self, stock = 1000):
        self.stock = stock

    def purchase_unit(self, units):
        print (f"purchased {units} from stock.")
        self.stock -= units
        print (f"current stock : {self.stock}.")

    def stock_units(self, units):
        print (f"stocked {units} to stock.")
        self.stock += units
        print (f"current stock : {self.stock}.")

    @classmethod
    def recharge_stock(cls, stock = 10):
        cls.stock = stock

lg = mobile(2000)
nokia = mobile(2000)
lg.purchase_unit(500)
# mobile.stock = 20
print (lg.stock)
print (nokia.stock)

mobile.recharge_stock()

print (lg.stock)
print (nokia.stock)
print (mobile.stock)