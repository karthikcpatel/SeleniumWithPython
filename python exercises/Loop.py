#1. Print first 10 natural numbers using while loop
i = 0
while i <= 10:
    print(i)
    i = i+1
#2. Accept number from user and print sum of all numbers from 1 till number entered by user
num = int(input("Enter the number: "))
for i in range(1,num):
    sum = 0
    sum = sum+i
    print(sum)
#3. Print multiplication table of given number
n = 2
for i in range(1, 11, 1):
    product = n*i
    print(product)
#4. Reverse a list using for loop
list1 = [10, 20, 30, 40, 50]
start = len(list1) - 1
stop = -1
step = -1
for i in range(start, stop, step) :
    print(list1[i])
#5. Given a list, iterate it, and display numbers divisible by five, and if number greater than 100, stop the iteration.
#6. Given a number, count total number of digits in the number Example - num=[10,30,60,90,120]
#7.Display nubers from -10 to -1 using for loop
for i in range(-10,-1,-1):
    print(i)
#8. Display message "Completed" after for loop
#9. Display Fibonacci series of given number
#10. Write for loop to get factorial of any given number
#11. Reverse a given number
#12.Using a loop print numbers that are present at even index positions
my_list = [10,20,30,40,50,60]
for x in range(1,len(my_list),2):
    print(my_list[x])
#13. Print following output
number_of_terms = 5
start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start, end=" ")
    sum += start
    start = (start * 10) + 2
print("\nSum of above series is:", sum)