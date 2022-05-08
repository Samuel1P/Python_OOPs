from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from itertools import count
from collections import namedtuple
import pytz


transact_op_map = {"withdrawal" : "W",
                   "deposit": "D",
                   "failed": "F",
                   "interest": "I"}
    
class TransactionNumber:
    """
    This class defines the Transaction Number objects properties
    """
    def __init__(self, code, user_tz):
        self.code = code
        self.user_tz = user_tz
        self.state = None
        self.account_number = None
        self.transact_utc_time = None
        self.user_time = None
        self._parse_code(self.code)
        
    def __str__(self) -> str:
        "user readable message for the transaction object"
        msg = (f"Account number: {self.account_number},\
               Transaction: {self.state},\
               User Time ({self.user_tz}): {self.user_time},\
               UTC time:  {self.transact_utc_time}")
        return msg
    
    def _parse_code(self, code):
        """
        Parses transtion code to human readable data.
        """
        code = code.split("-")
        self.state = code[0]
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
    """
    This class defines an Account, Interest rate and Account ops
    """
    transaction_id = count(1)
    _interest_rate = Decimal('1.07') # 7 percentage
    paise_rounding = Decimal('0.01')
    utc_time = lambda :datetime.utcnow()
    def __init__(self, acc_number, fname, lname, user_tz="UTC"):
        self._account_number = acc_number
        self._first_name = fname
        self._last_name = lname
        self._user_tz = user_tz
        self._balance = Decimal('0.00')
    
    @property
    def balance(self):
        return self._balance.quantize(Account.paise_rounding, ROUND_HALF_UP)
    
    @property
    def user_tz(self):
        return self._user_tz
    
    @user_tz.setter
    def user_tz(self, tz):
        if tz not in  pytz.all_timezones:
            raise ValueError(f"ERROR: Invalid time zone provided. Input: {tz}.")
        self._user_tz = tz
        return f"{self._first_name} {self._last_name} time zone updated to {tz}."
    
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    
    @classmethod
    def set_interest_rate(cls, new_percent):
        if not isinstance(new_percent, (int, float)) or new_percent <= 0: 
            raise ValueError(f"ERROR: Invalid interest rate provided. Input: {new_percent}.")
        
        new_rate = Decimal(new_percent).quantize(Account.paise_rounding, ROUND_HALF_UP)
        if new_rate == 0:
            new_rate = Decimal(0.00)
        else:
            new_rate = (100 + new_rate)/100
        print (f"Updating interest rate to {new_rate} %")
        cls._interest_rate = Decimal(new_rate)
        print (f"Interest rate is updated to {cls._interest_rate} %.")
    
    def withdraw_money(self, debit_amount):
        if debit_amount <=0:
            confirmation_code = self.generate_confirmation_code("failed")
            print (f"{self._first_name} {self._last_name} withdrawal of Rs.{debit_amount} is not permitted.\
                Transaction code : {confirmation_code}")
        elif debit_amount > self.balance:
            confirmation_code = self.generate_confirmation_code("failed")
            print (f"{self._first_name} {self._last_name} withdrawal of Rs.{debit_amount} failed due to insufficient balance.\
                Transaction code : {confirmation_code}")
        else:
            debit_amount = Decimal(debit_amount).quantize(Account.paise_rounding, ROUND_HALF_UP)
            confirmation_code = self.generate_confirmation_code("withdrawal")
            self._balance = self.balance - debit_amount
            print (f"{self._first_name} {self._last_name} withdrawed Rs.{debit_amount}.\
                Transaction code : {confirmation_code}")
        return confirmation_code
        
    def deposit_money(self, credit_amount):
        if credit_amount <=0:
            confirmation_code = self.generate_confirmation_code("failed")
            print (f"{self._first_name} {self._last_name} deposit of Rs.{credit_amount} is not permitted.\
                Transaction code : {confirmation_code}")
        else:
            credit_amount = Decimal(credit_amount).quantize(Account.paise_rounding, ROUND_HALF_UP)
            confirmation_code = self.generate_confirmation_code("deposit")
            self._balance = self.balance + credit_amount
            print (f"{self._first_name} {self._last_name} deposited Rs.{credit_amount}.\
                Transaction code : {confirmation_code}")
        print (confirmation_code)
        return confirmation_code
    
    
    def deposit_interest(self):
        if self.balance <= 0:
            confirmation_code = self.generate_confirmation_code("failed")
            print (f"{self._first_name} {self._last_name} has insufficient balance for Interest payment.\
                Transaction code : {confirmation_code}")
        elif Account._interest_rate == 0:
            confirmation_code = self.generate_confirmation_code("failed")
            print (f"{self._first_name} {self._last_name} Interest percentage is zero.\
                Transaction code : {confirmation_code}")
        else:
            current_balance = self.balance
            confirmation_code = self.generate_confirmation_code("interest")
            self._balance = current_balance * Account._interest_rate
            print (f"{self._first_name} {self._last_name} has an Interest payment deposit of Rs.{self.balance - current_balance}.\
                Transaction code : {confirmation_code}")
        print (confirmation_code)
        return confirmation_code
    
    def generate_confirmation_code(self, state):
        op = transact_op_map[state]
        time = str(Account.utc_time().strftime("%Y%m%d%H%M%S"))
        acc_number = str(self._account_number)
        count = next(Account.transaction_id)
        count = str(count)
        code = op+"-"+acc_number+"-"+time+"-"+count
        return code
    
    @staticmethod
    def parse_confirmation_code_namedtuple(code, tz="UTC"):
        #I-123-20220508174440-2
        TransactionCode = namedtuple("TransactionCode", "op account_number utc_time user_time transaction_id")
        parts = code.split("-")
        _op, _account_number, _utc_time, _transaction_id = parts
        op = _op
        account_number = int(_account_number)
        utc_time_dt = datetime.strptime(_utc_time, "%Y%m%d%H%M%S")
        old_timezone = pytz.timezone("UTC")
        new_timezone = pytz.timezone(tz)
        localized_timestamp = old_timezone.localize(utc_time_dt)
        _user_time_dt = localized_timestamp.astimezone(new_timezone)
        user_time = _user_time_dt.strftime('%Y-%m-%d %H:%M:%S')
        utc_time = utc_time_dt.strftime('%Y-%m-%d %H:%M:%S')
        transaction_id = int(_transaction_id)
        return TransactionCode(op, account_number, utc_time, user_time, transaction_id)
    
    
    @staticmethod
    def parse_confirmation_code_class(code, tz="UTC"):
        return TransactionNumber(code, tz)


print (f"{'#'*50} Script starts {'#'*50}") 
Tom = Account("123", "Tom", "Smith") # create account
print (f"Tom initial balance --> {Tom.balance}")
tracaction_code_one = Tom.deposit_money(100) # deposit 100 rs
print (f"Tom balance --> {Tom.balance}")
tracaction_obj_one = Account.parse_confirmation_code_class(tracaction_code_one, Tom.user_tz)
print (tracaction_obj_one)
print()
Tom.user_tz = ("Asia/Calcutta") # changing user time zone to IST
Tom_tracaction_two = Tom.withdraw_money(20) # withdraw 100 rs
print (f"Tom balance --> {Tom.balance}")
Tom_tracaction_two = Account.parse_confirmation_code_class(Tom_tracaction_two, Tom.user_tz)
print (Tom_tracaction_two)
print()
Tom_tracaction_three = Tom.deposit_interest() # deposit interest to balance
print (f"Tom balance --> {Tom.balance}")
Tom_tracaction_three = Account.parse_confirmation_code_class(Tom_tracaction_three, Tom.user_tz)
print (Tom_tracaction_three)
print()
Tom_tracaction_four = Tom.withdraw_money(2235) # withdraw 2235 rs
print (f"Tom balance --> {Tom.balance}")
Tom_tracaction_four = Account.parse_confirmation_code_class(Tom_tracaction_four, Tom.user_tz)
print (Tom_tracaction_four)
print()
Tom_tracaction_five = Tom.deposit_money(0) # deposit 0 rs
print (f"Tom final balance --> {Tom.balance}")
Tom_tracaction_five = Account.parse_confirmation_code_class(Tom_tracaction_five, Tom.user_tz)
print (Tom_tracaction_five)
print()
Account.set_interest_rate(14) # increase deposit interest
Tom_tracaction_six = Tom.deposit_interest() # deposit interest to balance
print (f"Tom_tracaction_six --> {Tom_tracaction_six}")
print (f"Tom balance --> {Tom.balance}")
Tom_tracaction_six = Account.parse_confirmation_code_namedtuple(Tom_tracaction_six, 'Australia/Perth')
print (f"Transaction six - op : {Tom_tracaction_six.op}")
print (f"Transaction six - custom user_time: {Tom_tracaction_six.user_time}")
print (f"Transaction six - utc_time: {Tom_tracaction_six.utc_time}")
print (f"Transaction six - transaction_id : {Tom_tracaction_six.transaction_id}")
print (f"Transaction six - account_number : {Tom_tracaction_six.account_number}")
print()
print (f"{'#'*50} Script Completion {'#'*50}") 