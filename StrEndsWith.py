f""" Complete the solution so that it returns true if the first argument(string)
 passed in ends with the 2nd argument (also a string)."""
def solution(text, ending):
    #use the .endswith() built in python function
    return text.endswith(ending)

print(solution( "samurai", "ai"    ))
print(solution( "ninja",   "ja"    ))
print(solution( "sensei",  "i"     ))
print(solution( "abc",     "abc"   ))
print(solution( "abcabc",  "bc"    ))
print(solution( "fails",   "ails"  ))