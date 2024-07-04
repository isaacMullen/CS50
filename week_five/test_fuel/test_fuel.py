import pytest
from fuel import convert, guage

#testing convert()'s error raises and normal function
def test_convert():
    assert convert("1/2") == 50
def test_convert1():
    with pytest.raises(ValueError):
        convert("2/1")
def test_convert2():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

#testing guage()'s normal functions. errors are caught with convert()
def test_guage():
    assert guage(99) == "F"
def test_guage1():
    assert guage(1) == "E"
