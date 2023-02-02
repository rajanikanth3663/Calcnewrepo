def add(x,y):
    """_summary_
Add function
    """
    return x+y

def subtract(x,y):
    """_summary_
Subtract function
    """
    return x-y

def multiply(x,y):
    """_summary_
Multiply function
    """
    return x*y

def divide(x,y):
    """_summary_
Divide function
    """
    if(y==0):
        raise ValueError('cannot divide by zero!')
    return x/y