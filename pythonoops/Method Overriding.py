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