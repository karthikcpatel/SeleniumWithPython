class GrandParent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printGrandParent(self):
        print(self.name, self.age)

    def printHelloWorld(self):
        print("Hey! This is hello world from grand parent class")

class Parent:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printParent(self):
        print(self.name, self.age, self.salary)

    def printHelloWorld(self):
        print("Hey! This is hello world from parent class")

class Child(Parent, GrandParent):
    pass

x = Child("Chetan","Patel",50000)
x.printGrandParent()
x.printHelloWorld()

#y = Child("Dhanji",85, 15)
#y.printParent()
#y.printHelloWorld()