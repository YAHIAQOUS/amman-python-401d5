def factorial(n):
    if n <= 1:
        return int(1)
    return n * factorial( n - 1 )    



# 5! = 5 x (5 - 1)
# 5! = 5 x 4! 

# 4! = 4 x (4 - 1 )
# 4! = 4 x 3!

# 3! = 3 x (3 - 1)
# 3! = 3 x 2! 

# 2! = 2 ( 2 - 1 )
# 2! = 2 x 1! 

# 1! = 1 x (1 - 1)
# 1! = 0! 

# 0! = 1  
