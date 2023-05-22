#Clock shows h hours, m minutes and s seconds after midnight.

#Your task is to write a function which returns the time since midnight in milliseconds.


def past(h, m, s):
    #can use true value given time is not reset by noon in this example
    #we start with s knowing that there are 1000 milliseconds per second
    s = s * 1000
    #with 60 s in a m we complete the same operation but multiply by 60
    m = m * (60*1000)
    #with 60 m being in an h, we repeat the process nesting the operation
    h = h * (60 * (60*1000))
    #finally return the sum of all h, m, and s
    return h + m + s


print(past(1, 2, 34))
print(past(0, 0, 50))