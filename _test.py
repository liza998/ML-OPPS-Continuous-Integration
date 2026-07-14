# pytest is a testing process in python

import pytest

def square(n):
    return n**2 

def cube(n):
    return n**3 

def fifth_power(n):
    return n**5

# Testing the square  of function by using assert which works like IF condition
#assert statement: assert checks whether a condition is True. If it is False, Python immediately raises an AssertionError.
# assert condition, "Error message"
def test_square():
    assert square(2) == 4 , "Test Failed: square of 2 should be 4"
    assert square(3) == 9, "Test Failed: square of 3 should be 9"

def test_cube():
    assert cube(2) == 8 , "Test Failed: cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: cube of 3 should be 27"

def test_fifth_power():
    assert fifth_power(2) ==  32, "Test Failed: fifth_power of 2 should be 32"
    assert fifth_power(5) == 3125, "Test Failed: fifth_power of 5 should be 3125"
