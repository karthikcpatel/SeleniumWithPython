print("Enter first number: ")
num1 = input()

print("Enter second number: ")
num2 = input()

try:
     print("Sum of these two numbers is: ", int(num1)+int(num2))
except Exception as e:
     print(e)
finally:
     print("I will always be executed")

try:
   fh = open("testfile", "r")
   fh.write("This is my apple file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

try:
   fh = open("testfile", "r")
   fh.write("This is my apple file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
finally:
   print ("Written content in the file successfully")