# A variable created under a function
def my_func():
    x = 10
    print(x)
my_func()

def my_func1():
    x = 20
    def my_innerfunc():
        print(x)
    my_innerfunc()
my_func1()


# A variable outside function can be accessed from anywhere
y = 30
def myfunc2():
  print(y)
myfunc2()

# Global variable vs local variable
a = 300
def myfunc4():
  a = 200
  print(a)
myfunc4()
print(a)

# If global keyword is used that variable will become accessed from anywhere.

# The value of local variable inside a function can be overridden.
kp = "Kartik"
def myfunc():
  global kp
  kp = "Dipika"
myfunc()
print(kp)