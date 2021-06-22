from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation as valid

def test_version():
    assert __version__ == '0.1.0'

def test_multi_bracket_validation_all_conditions():
    assert valid('{}') == True
    assert valid('{}(){}') == True
    assert valid('()[[Extra Characters]]') == True
    assert valid('(){}[[]]') == True
    assert valid('{}{Code}[Fellows](())') == True
    assert valid('[({}]') == False
    assert valid('(](') == False
    assert valid('{(})') == False