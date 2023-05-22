f"""Timmy & Sarah think they are in love, but around where they live, 
they will only know once they pick a flower each. If one of the flowers 
has an even number of petals and the other has an odd number of petals it 
means they are in love.

Write a function that will take the number of petals of each flower and 
return true if they are in love and false if they aren't."""

def lovefunc( flower1, flower2 ):
    #sounds like a classic "and" boolean
    #start by sigling out the result they don't want
    #petals determin if the flowers have even or odd petals
    petals1 = flower1 % 2
    petals2 = flower2 % 2
    if petals1 == 1 and petals2 == 1 :
        return False
    elif petals1 == 0 and petals2 == 0:
        return False
    else:
        return True
    
print(lovefunc(7,9))
print(lovefunc(2,3))
print(lovefunc(4,6))
print(lovefunc(5,4))