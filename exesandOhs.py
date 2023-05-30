"""
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    #make all letter the same casing
    s = s.lower()
    #use pythons .count() functions to avoid loops
    countx =  s.count("x")
    counto = s.count("o")
    #return boolean
    return countx == counto

print(xo("ooxx"))
print(xo("ox0"))
print(xo("xxxoo"))
print(xo("OXoxOXoX"))