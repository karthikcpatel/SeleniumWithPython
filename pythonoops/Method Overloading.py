def sum(a, b):
    x = a + b
    print(x)

def product(a, b, c):
    x = a + b + c
    print(x)

#product(5,5)

product(5, 5, 5)

class Human:

    def sayHello(self,name=None):
        if name is not None:
            print('Hello ' +name)
        else:
            print('Hello ')

obj = Human()
obj.sayHello()
obj.sayHello("Kartik")