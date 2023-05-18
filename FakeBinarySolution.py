#Given a string of digits, you should replace any digit 
#below 5 with '0' and any digit 5 and above with '1'. 
#Return the resulting string.

def fake_bin(x):
    #strlist = list(x)
    #turns string of nums into int list for binary
    numlist = list(map(int, x))
    #take int list and turn into binary list
    binarylist = [0 if num < 5 else 1 for num in numlist]
    #join the list back into a string
    binarystr = ''.join(map(str, binarylist))
    
    return str(binarystr)

print(fake_bin("5746329283"))