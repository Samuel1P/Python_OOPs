"""
default test file
"""
import pytest
class TestDefatult:
    @pytest.mark.success
    def test_defalt_true(self):
        assert True == True
    
    @pytest.mark.fail
    def test_defaul_false(self):
        assert True == False, "True can never be false"
        