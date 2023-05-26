#create a function that returns the middle character of a string
# if it's even then return the two middle characters

def get_middle(s):
    #make global variable for index number
    x = len(s)/2
    #x-1 because of 0 index and not 1 index
    if len(s)%2 == 0:
        return s[int(x-1)] + s[int(x)]
    if len(s)%2 == 1:
        return s[int(x)]
    

print(get_middle("test"))
print(get_middle("ttttmmtttt"))
print(get_middle("123456789"))