f"""Given a random non-negative number, you have to return the digits 
of this number within an array in reverse order."""

def digitize(n):
    #have to convert to string
    n = str(n)
    #then list
    n = list(n)
    #reverse list
    m = n[::-1]
    #return string numbers back to int using map function.
    m = list(map(int, m))
    return m
print(digitize(987654321))
print(digitize(123456789))