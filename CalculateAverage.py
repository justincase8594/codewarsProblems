f"""Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0. """

from statistics import mean
#have to be mindful of the StatisticsError
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    
    return mean(numbers)

print(find_average([1, 2, 3]))
print(find_average([12, 24, 36]))
print(find_average([]))
