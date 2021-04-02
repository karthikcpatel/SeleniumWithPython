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
# changing age using setter
obj.setAccess(123456)
obj.getAccess()