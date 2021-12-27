# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.
# Lambda functions reduces the line of code.
# They are generally used when a function is used temporarily for a short period.

def add(x,y):
    return x+y
print(add(5,5))

add = lambda x,y,z : x+y+z
print(add(5,5,5))