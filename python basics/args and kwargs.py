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