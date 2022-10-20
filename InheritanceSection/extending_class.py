

class Account:
    interest_rate = 4.0
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Generic"
    
    def calculate_interest(self):
        # Account.interest_rate if you want all child class to follow the same rate
        # self.interest_rate if you want child class interest_rate to be used but this opens up dev to modify the instance attribute self.interest_rate of the class instance.
        # self.__class__.interest_rate to always honor child class interest_rate and not get affected by changes in instance attribute.
        return f"Interest for {self.account_type} account is {self.__class__.interest_rate}%" 
    

class SavingsAccount(Account):
    interest_rate = 6.0
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Savings"

a = Account(12, 1500)
#print(a.calculate_interest())

s = SavingsAccount(15,2000)
s.interest_rate=10
print(s.calculate_interest())