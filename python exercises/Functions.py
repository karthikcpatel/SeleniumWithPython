#1. Create a function that can accept two arguments name and age and print its value

#2. Write a function func1() such that it can accept a variable length of  argument and print all arguments value
# Input:
#func1(20, 40, 60)
#func1(80, 100)
# Output:
#func1(20, 40, 60)
#20
#40
#60

#func1(80, 100)
#80
#100

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#3. Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call
# Input: 40 and 10
# Output: 50, 30
def calculation(a, b):
    return a+b, a-b

res = calculation(40, 10)
print(res)

#4. Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 to salary
#showEmployee("Kartik", 10000)
#showEmployee("Kartik")

def showEmployee(name, salary=9000):
    print("Employee", name, "Salary is:", salary)

showEmployee("Kartik", 9000)
showEmployee("Kartik")

#5. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def outerFun(a,b):
    pass
    def innerFun(a,b):
        return a+b
    add = innerFun(a,b)
    return add+5

result = outerFun(5,10)
print(result)

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)

#6. Assign a different name to function and call it through the new name
def displayStudent(name, age):
    print(name, age)

displayStudent("Kartik", 30)

#You should be able to call the same function using
showStudent = displayStudent
showStudent("Nirav", 30)

#7. Create a Python list to print all even numbers between 4 and 30
#Output: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print(list( range(4, 30, 2)))

#8. Return the largest item from the given list
#Input: aList = [4, 6, 8, 24, 12, 2]
aList = [4, 6, 8, 24, 12, 2]
print(max(aList))
