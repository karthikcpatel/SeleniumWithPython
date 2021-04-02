# _name_ is a special variable. If source file is executed as main program, interpreter sets _name_ variable to _main_
# If being imported from another module, _name_ will be set to module's name.

class Parent:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def add(self,a,b):
        if __name__ == '_main_':
            print(a+b)

x = Parent("Chetan", "Patel")
x.printname()
x.add(5,5)
print(__name__)