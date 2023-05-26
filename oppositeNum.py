#Very simple, given an integer or a floating-point number, 
#find its opposite.

def opposite(number):
    if number == 0:
        return 0
    #any number you multiply by -1 will give you the opposite number
    else:
        number = number * -1
        return number
    
print(opposite(14))
print(opposite(-56))
print(opposite(0))