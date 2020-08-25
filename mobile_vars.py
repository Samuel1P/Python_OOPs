class mobile:
    stock = 1000
    def purchase_unit(self, units):
        print (f"purchased {units} from stock.")
        self.stock -= units
        print (f"current stock : {self.stock}.")

    def stock_units(self, units):
        print (f"stocked {units} to stock.")
        self.stock += units
        print (f"current stock : {self.stock}.")





print (mobile.__dict__)
lg = mobile()
nokia = mobile()
lg.purchase_unit(500)
print (lg.__dict__)
mobile.stock = 20
print (lg.stock)
print (nokia.stock)
print (mobile.__dict__)

