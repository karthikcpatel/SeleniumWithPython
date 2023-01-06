def sum(a, b):
    x = a + b
    print(x)

def sum(a, b, c):
    x = a + b + c
    print(x)

#product(5,5)

sum(5, 5, 5)

class Human:

    def sayHello(self,name=None):
        if name is not None:
            print('Hello ' +name)
        else:
            print('Hello ')

obj = Human()
obj.sayHello()
obj.sayHello("Kartik")

print("********** Second Example **********")

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))