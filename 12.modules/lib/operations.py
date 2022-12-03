def sum(num1, num2):
    return num1 + num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

def power(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    return num1 % num2

def floor(num1, num2):
    return num1 // num2

def op(num1, num2, operation):
    if operation == '+':
        return sum(num1, num2)
    elif operation == '*':
        return multiple(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '**':
        return power(num1, num2)
    elif operation == '%':
        return remainder(num1, num2)
    elif operation == '//':
        return floor(num1, num2)
    else:
        return 'Invalid operation'