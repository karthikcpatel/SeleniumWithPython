# We can protect our data. We can set the variables as read and write-only.

class Employee:
    def __init__(self, name, accessId):
        self.name = name
        self.__accessId = accessId

    def printDetails(self):
        print(self.name)
        print(self.__accessId)

    def setAccess(self, accessId):
        self.__accessId = accessId

    def getAccess(self):
        print(self.__accessId)

obj = Employee('Kartik', 501245)
# accessing using class method
obj.printDetails()
print(obj.name)
# changing age using setter
obj.setAccess(123456)
obj.getAccess()

print("********** Second Example **********")

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.n = name
        # private member
        self.sal = salary

# creating object of a class
emp = Employee('Kartik', 10000)

# accessing private data members
print('Salary:', emp.n, emp.sal)

print("-------------------------------------------------------")

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Kartik', 10000)

# accessing private data members
print('Salary:', emp.__salary)

print("---------------------------------------------")
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def get(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Kartik', 10000)

# calling public method of the class
emp.get()
