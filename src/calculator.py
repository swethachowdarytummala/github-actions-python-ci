def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if(b == 0):
        return ValueError("Cannot divided by zero")
    return a / b
