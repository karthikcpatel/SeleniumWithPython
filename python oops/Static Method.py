class Employee:

    companyName = "Citi"

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printAllDetails(self):
        print(self.fname,self.lname)

    @staticmethod
    def printAll(string):
        print("Hello " +string)

obj = Employee("Kartik","Patel")
obj.printAllDetails()
Employee.printAll("Everyone")