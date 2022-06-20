"""
default test file
"""
import pytest
class TestDefatult:
    def test_defalt_true(self):
        assert True == True
    
    @pytest.mark.xfail
    def test_defaul_false(self):
        assert True == False, "True can never be false"
        