# Creating and calling a function
def my_name():
    print("My name is Kartik")
my_name()

# Function that accepts arguments
def name(fname,lname):
    print(fname,lname)
name("Kartik","Patel")

# return in python
def add(x, y):
    result = x + y
    return result

output = add(5, 4)
print(f'Output of add(5, 4) function is {output}')

# yield in python
def add(x, y):
    result = x + y
    yield result

output = add(5, 4)
print(f'Output of add(5, 4) function is {output}')
for i in output:
    print(i)

# None in python function
# The None keyword is used to define a null variable or an object. Its data type would be NoneType
var = None
if var is None:
    print("var has value None")
else:
    print("var has some value")

# Function having static parameters
def student_name(a,b,c,d,e):
    print(a,b,c,d,e)
student_name("kartik","shilpi","chetan","payal","bhavyesh")

# *args in function
# Passing list to a function
def company_employees(*args):
    for x in args:
        print(x)
employees = ["prashant","kartik","maulik","nikhil"]
company_employees(*employees)

# **kwargs in function
#passing dictionary to a function
def college_students(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
students = {"Kartik":"Patel","Payal":"Patel"}
college_students(**students)

# Default parameter Value
def my_function(name="Kartik"):
    print("My name is " +name)
my_function("Bhavyesh")
my_function("Aishwariya")
my_function()

# Arbitrary arguments
def greet(*names):
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

greet("Monica", "Luke", "Steve", "John")

# Recursive function
def fac(n):
    if n==1:
        return 1 # Base Case
    else:
        return n*fac(n-1)

print(fac(3))