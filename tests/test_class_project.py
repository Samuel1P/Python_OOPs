"""
Test Suite for the Class section projects solution
"""
import pytest
from ClassesSection.Project_classes_solution.project_class_solution import Account



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
        
    def teardown_method(self):
        del self.test_account