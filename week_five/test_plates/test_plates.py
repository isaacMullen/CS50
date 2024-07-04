from plates import is_valid

def test_default():
    assert is_valid() == True

def test_case_three():
    assert is_valid("aaaaaaa") == False

def test_case_one():
    assert is_valid("aa23bc") == False

def test_case_two():
    assert is_valid("123456") == False

def test_case_four():
    assert is_valid("21abbbc") == False

def test_case_five():
    assert is_valid("aabbc0") == False
