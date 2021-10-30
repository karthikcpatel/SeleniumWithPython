# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
reverse_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    reverse_number = (reverse_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(reverse_number))

num1 = '364'
num2 = '1836'

# Approach 1:
def solution(num1, num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))

print(solution(num1, num2))