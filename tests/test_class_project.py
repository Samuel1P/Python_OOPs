"""
Test Suite for the Class section projects solution
"""
import pytest
from ClassesSection.Project_classes_solution.project_class_solution import Account
from tests.TestLogger import get_logger_instance, log_info, log_error, log_warn, log_debug


log = get_logger_instance(__name__)


class TestBankingProject:
    """
    Test Class
    """
        
    def setup_method(self):
        """
        setup method to run before the start of each test.
        """
        acc_number = 1
        fname = "Robert"
        lname = "Kenny"
        user_tz = "UTC"
        self.test_account = Account(acc_number=acc_number, fname=fname, lname=lname, user_tz=user_tz)
    
    def test_create_account(self):
        assert self.test_account.account_number == 1
        assert self.test_account.first_name == "Robert"
        assert self.test_account.last_name == "Kenny"
        assert self.test_account.user_tz == "UTC"
        
    def test_change_accounts_timezone(self):
        self.test_account.user_tz = "Asia/Kolkata"
        assert self.test_account.user_tz == "Asia/Kolkata"
        
    def test_check_initial_balance(self):
        assert self.test_account.balance == 0
    
    def test_check_initial_balance(self):
        assert self.test_account.balance == 0
        
    def test_credit_amount(self):
        self.test_account.deposit_money(100)
        assert self.test_account.balance == 100
    
    def test_debit_amount(self):
        self.test_account.deposit_money(100)
        self.test_account.withdraw_money(60)
        assert self.test_account.balance == 40
    
    def test_insufficient_balance(self):
        assert self.test_account.balance == 0
        conf_code = self.test_account.withdraw_money(60)
        assert conf_code.startswith("F-")
        assert self.test_account.balance == 0
            
    def teardown_method(self):
        del self.test_account
