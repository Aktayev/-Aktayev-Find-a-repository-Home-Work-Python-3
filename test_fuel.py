from fuel import convert, gauge
import pytest

# def main():

def test_convert():
    assert convert("1/99") == 1
    assert convert("99/100") == 99
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value():
    with pytest.raises(ValueError):
        convert("dog")