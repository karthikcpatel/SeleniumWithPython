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