from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import pytz

class WithdrawalDeclinedError(Exception):
    def __init__(self, msg):
        self._msg = msg
        pass
        
class TransactionNumber:
    transact_map = {"W": "Withdrawal",
                    "D": "Deposit",
                    "X": "Declined Withdrawal",
                    "I": "Interest Deposit"}
    def __init__(self, code, user_tz) -> None:
        self.code = code
        self.user_tz = user_tz
        self.state = None
        self.account_number = None
        self.transact_utc_time = None
        self.user_time = None
        self._parse_code(self.code)

    def __repr__(self) -> None:
        print (f"Account number: {self.account_number}, Transaction: {self.state}, User Time ({self.user_tz}): {self.user_time} {self.user_tz}, UTC time:  {self.transact_utc_time}")
        
    def __str__(self) -> str:
        return (f"Account number: {self.account_number}, Transaction: {self.state}, User Time ({self.user_tz}): {self.user_time}, UTC time:  {self.transact_utc_time}")
    
    def _parse_code(self, code):
        code = code.split("-")
        self.state = TransactionNumber.transact_map[code[0]]
        self.account_number = code[1]
        transact_utc_time = code[2]
        self.transact_utc_time = datetime.strptime(transact_utc_time, "%Y%m%d%H%M%S")
        old_timezone = pytz.timezone("UTC")
        new_timezone = pytz.timezone(self.user_tz)
        localized_timestamp = old_timezone.localize(self.transact_utc_time)
        self.user_time = localized_timestamp.astimezone(new_timezone)
        self.user_time = self.user_time.strftime('%Y-%m-%d %H:%M:%S')
        self.transact_utc_time = self.transact_utc_time.strftime('%Y-%m-%d %H:%M:%S')
        
class Account:
    count = 0
    interest_rate = Decimal('1.07') # 7 percentage
    paise_rounding = Decimal('0.01')
    utc_time = lambda :datetime.utcnow()
    def __init__(self, acc_number, fname, lname, tz="UTC") -> None:
        self._account_number = acc_number
        self._first_name = fname
        self._last_name = lname
        self._balance = Decimal('0.00')
        self._user_tz = tz
        
    
    @property
    def user_tz(self):
        return self._user_tz
    
    @user_tz.setter
    def user_tz(self, tz):
        if tz not in pytz.all_timezones:
            raise Exception(f"Error: Invalid timezone : {tz}")
        self.user_time = tz
        self._user_tz = tz
        
    @property
    def balance(self):
        return self._balance.quantize(Account.paise_rounding, ROUND_HALF_UP)
    
    def withdraw_money(self, debit_amount):
        if debit_amount > self.balance:
            # we can raise execption here
            confirmation_code = self.generate_confirmation_code("X")
        else:
            debit_amount = Decimal(debit_amount).quantize(Account.paise_rounding, ROUND_HALF_UP)
            self._balance = self.balance - debit_amount
            confirmation_code = self.generate_confirmation_code("W")
        print (confirmation_code)
        return confirmation_code        
        
    def deposit_money(self, credit_amount):
        credit_amount = Decimal(credit_amount).quantize(Account.paise_rounding, ROUND_HALF_UP)
        self._balance = self.balance + credit_amount
        confirmation_code = self.generate_confirmation_code("D")
        print (confirmation_code)
        return confirmation_code
    
    
    def deposit_interest(self):
        self._balance = self.balance * Account.interest_rate
        confirmation_code = self.generate_confirmation_code("I")
        print (confirmation_code)
        return confirmation_code
        
    
    def generate_confirmation_code(self, state):
        time = str(Account.utc_time().strftime("%Y%m%d%H%M%S"))
        acc_number = str(self._account_number)
        Account.count = Account.count + 1
        count = str(Account.count)
        code = state+"-"+acc_number+"-"+time+"-"+count
        return code
    
    @classmethod
    def parse_confirmation_code(cls, code, tz):
        return TransactionNumber(code, tz)

print ("*"*100)        
Sam = Account("123", "Samuel", "I P")
Sam.user_tz = ("UTC")
Sam.deposit_money(100)
print (f"Sam balance --> {Sam.balance}")
Sam.deposit_money(0.00499)
print (f"Sam balance --> {Sam.balance}")
tracact_obj = Account.parse_confirmation_code(Sam.deposit_money(2235), Sam.user_tz)
print (str(tracact_obj))
print (tracact_obj.__dict__)
print (f"Sam balance --> {Sam.balance}")
Sam.user_tz = ("Asia/Calcutta")
tracact_obj1 = Account.parse_confirmation_code(Sam.deposit_interest(), Sam.user_tz)
print (str(tracact_obj1))
print (tracact_obj1.__dict__)
print (f"Sam balance --> {Sam.balance}")
# Tom = Account("12343", "Tom", "Evans")
# Tom.withdraw_money(2235)
# tracact_obj = Tom.parse_confirmation_code(Tom.deposit_money(2235))
# print (str(tracact_obj))
# print (tracact_obj.__dict__)
# Tom.user_tz = ("Asia/Calcutta")
# import time;time.sleep(3)
# print()
# tracact_obj2 = Tom.parse_confirmation_code(Tom.withdraw_money(2238))
# print (str(tracact_obj2))
# print (tracact_obj2.__dict__)
print ("#"*100)