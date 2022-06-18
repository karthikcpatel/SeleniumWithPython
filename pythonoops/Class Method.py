class Employee:
    companyName = "S&P Global"
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printAllDetails(self):
        print(self.fname,self.lname)

    @classmethod
    def callCompanyName(cls):
        return cls.companyName

    @classmethod
    def emp_details(cls,newCompany):
        cls.companyName = newCompany
        print(newCompany)

obj = Employee("Kartik","Patel")
obj.printAllDetails()
print(Employee.callCompanyName())
Employee.emp_details("Amazon")
