from bank import value

def test_default():
    assert value() == 0

def test_arg1():
    assert value("hello") == 0

def test_arg2():
    assert value("hey") == 20

def test_arg3():
    assert value("yo") == 100