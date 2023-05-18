# In this simple assignment you are given a number and
# have to make it negative. But maybe the number is 
# already negative?

def make_negative( number ):
    if number < 0:
        return number
    else:
        number = number * -1
        return number
    
print(make_negative(-9))
print(make_negative(9))
print(make_negative(0))