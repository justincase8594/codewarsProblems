#Given an integral number, determine if it's a square number:

import math

def is_square(n):
    #.isqrt() will cause error for negative numbers
    if n < 0:
        return False
    #after error avoided, test square root and format for return boolean
    else:
        sqroot = math.isqrt(n)
        return sqroot**2 == n
    
print(is_square(-1))
print(is_square(0))
print(is_square(25))
print(is_square(26))