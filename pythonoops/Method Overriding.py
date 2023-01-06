class Parent:

    def defaultMethod(self):
        print("Hey! I am from parent class")

class Child(Parent):

    def defaultMethod(self):
        print("Hey! I am from the child class")

x = Child()
x.defaultMethod()
y = Parent()
y.defaultMethod()

print("********** Second example **********")


class India():
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")


class USA(India):
    def capital(self):
        print("Washington, D.C.")

    def language(self):
        print("English")

    def car(self):
        print("Tesla")


obj_ind = India()
obj_usa = USA()
obj_usa.capital()