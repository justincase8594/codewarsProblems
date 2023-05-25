#You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20

def positive_sum(arr):
    #see if list is empty first
    if len(arr) == 0:
        return 0
    #create new list with only positive numbers
    positiveList = [num for num in arr if num >=0]
    return sum(positiveList)

print(positive_sum([4, 6, -5, -7, 5, 4, 2, -2, -1, 3]))