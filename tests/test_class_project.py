"""
Test Suite for the Class section projects solution
"""
from ClassesSection.Project_classes_solution import project_class_solution

class TestBankingProject:
    """
    Test Class
    """
    def setup_class(self):
        """setup class to run before the start of first test.
        """
        self.transact_map = project_class_solution.transact_op_map
        self.Account = project_class_solution.Account
        self.TransactionNumber = project_class_solution.TransactionNumber
        
    
    