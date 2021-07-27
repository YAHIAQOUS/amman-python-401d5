from fizz_buzz import __version__

from fizz_buzz.fizz_buzz import fizz_buzz, list_fizz_buzz, dict_fizz_buzz#subject of test 
 



def test_version():
    assert __version__ == '0.1.0'



# def test_one(): #unit test
#     #arrange
#     expected = '1'
#     #assign 
#     actual = fizz_buzz(1)
#     #assert 
#     assert expected == actual 

# def test_two(): #unit test
#     #arrange
#     expected = '2'
#     #assign 
#     actual = fizz_buzz(2)
#     #assert 
#     assert expected == actual 

# def test_three():
#     #arrange 
#     expected = 'Fizz'
#     #assign 
#     actual = fizz_buzz(3)
#     #assert 
#     assert expected == actual

# def test_five(): 
#     expected = 'Buzz'
#     actual = fizz_buzz(5)
#     assert expected == actual


# def test_fifteen(): 
#     expected = 'FizzBuzz'
#     actual = fizz_buzz(15)
    
#     assert expected == actual
    
    
def test_list():
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'FizzBuzz']
    
    actual = list_fizz_buzz([1, 2, 3, 4, 5, 15])
    
    assert expected == actual 
    

def test_dict(): 
    expected = {
        1 : '1',
        2 : '2', 
        3 : 'Fizz',
        4 : '4', 
        5 : 'Buzz',
        45: 'FizzBuzz'
    }
    
    actual = dict_fizz_buzz([1, 2, 3, 4, 5, 45])
    
    assert expected == actual
    
# if expected('1') is equal in type and value to actual('whatever value it holds) return True(pass the test) 
# else return false (Fail the test)
# fizz_buzz(number)

# 1 
# 2
# Fizz
# buzz 
# FizzBuzz  