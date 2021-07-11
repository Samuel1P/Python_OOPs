class phone:
    promo1 = 0.90
    promo2 = 0.70
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_offer(self, offer):
        new_price = self.price
        if offer == 1:
            new_price = self.price * self.promo1
        elif offer == 2:
            new_price = self.price * self.promo2
        return new_price

class op(phone):
    promo1 = 0.50
    def __init__(self, brand, model, price, year):
        super().__init__(brand, model, price)
        self.year = year
    def get_year(self):
        return f" {self.brand} released in {self.year}"


obj = phone("one plus", "5t", 25000)
op_obj = op("one plus", "5t", 25000, 2020)


print (obj.get_offer(2))
print (obj.get_offer(1))
print (op_obj.get_year())
print (op_obj.get_offer(1))
print (op_obj.get_offer(2))
