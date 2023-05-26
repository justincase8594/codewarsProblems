#Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.
#op = operation, val1 = value1, val2 = value2
def basic_op(op, val1, val2):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == "*":
        return val1 * val2
    else:
        return val1 / val2
    

print(basic_op("*", 9, 16))
print(basic_op("/", 9, 16))
print(basic_op("+", 9, 16))
print(basic_op("-", 9, 16))