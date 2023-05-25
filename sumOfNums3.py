#Given two integers a and b, which can be positive or negative, 
#find the sum of all the integers between and including them 
#and return it. If the two numbers are equal return a or b.

def get_sum(a,b):
    if a == b:
        return a
    # use range and sum function to get right outputs
    #make sure the first number is less than the second
    if a <= b:
        #add +1 to higher number or it won't count the last number
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
    
print(get_sum(-46, 86))
print(get_sum(453, -186))
print(get_sum(-4, 4))