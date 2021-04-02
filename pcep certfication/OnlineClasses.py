def company_employees(*args):
    for x in args:
        print(x)
employees = ["virat","rohit","bhuvi"]
company_employees(*employees)

def students(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
students_details = {"Kartik":"Patel","Aishwarya":"lastname"}
students(**students_details)