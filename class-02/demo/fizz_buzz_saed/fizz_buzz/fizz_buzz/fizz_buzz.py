def fizz_buzz(number): 
    """
    if the number is dividable by 3 return Fizz 
       if the number is dividable by 5 return Buzz 
       if the number is dividable by 3 and 5 return FizzBuzz 

    Args:
        number ([integer]): [an integer to check]

    Returns:
        [string]: [if it falls under the rules it will eitehr be Fizz or buzz Or fizzBuzz]
    """
    
    if not number % 15 : 
        return 'FizzBuzz'
    
    elif not number % 3: 
        return 'Fizz'

    elif not number % 5 : 
        return 'Buzz'
    
    return str(number)

 
 
 

def list_fizz_buzz(numbers: list) -> list: 
    """ 
    We take a list of numbers and we change its content (elements) follwing the FizzBuzz rules to
    
    input -> list of integers 
    
    output -> list of strings 
       
    
    """
    
    # output = []
    
    # for num in numbers:
    #     output.append(fizz_buzz(num))
        
    # return output
        
    return [fizz_buzz(num) for num in numbers]
        
         
        
    
    
def dict_fizz_buzz(numbers: list) -> dict:
    
    # output = {}
    # for num in numbers:
    #     output[num] = fizz_buzz(num)
        
    # return output
    return {num:fizz_buzz(num) for num in numbers}
    