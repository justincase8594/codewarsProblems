#Given an array of integers, return a new array with 
#each value doubled.
def maps(a):
    a = [num*2 for num in a]
    return a

testlist = [1, 2, 3, 4, 5]
print(maps(testlist))