class Employee:
    class_var = "Class variable is being called"
    def __init__(self,name,age):
       self.name = name
       self.age = age

    def emp_dep(self,dept,title):
        self.fname = dept
        self.lname = title
        self.inst_var = "Instance variable is being called"

obj = Employee("Kartik", "Patel")
obj.emp_dep("QE","SDET")
print(obj.fname)
print(obj.lname)
print(obj.name)
print(obj.age)
print(Employee.class_var)
print(obj.inst_var)
