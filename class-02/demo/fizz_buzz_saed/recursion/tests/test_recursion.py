from recursion import __version__

from recursion.recursion import  factorial

def test_version():
    assert __version__ == '0.1.0'



def test_one():
    expected = 1 
    
    actual = factorial(1)

    assert  expected == actual


def test_two():
    expected = 2 
    
    actual = factorial(2)
    
    assert expected == actual
    

def test_five():
    expected = 120 
    
    actual = factorial(5)

    assert expected == actual

# 120 