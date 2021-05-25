#1. Given two integers return their sum. If summation of both numbers is greater than 100 retrun their average.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1+num2
average = (num1+num2)//2
if (num1+num2 < 100):
    print("The summation of two numbers is: ", sum)
else:
    print("The average of two numbers is: ", average)

#2. Given a range of first 10 numbers. Iterate from start number to end number, and in each iteration print sum of current and previous number
previous = 0
for i in range(1,11):
    sum = previous + i
    print("The current number is: ", i, "The previous number is: ", previous, "The summation is: ", sum)
    previous = i

#3. Given a string, display only those characters that are present at even index number.
string = "hippopotamus"
for i in range(1,len(string),2):
    print(string[i])

#4. Given list of number return True if first and last number of list are same
list = [10,20,30,40,50,10]
first = list[0]
last = list[-1]
if first==last:
    print("True")
else:
    print("False")

#5. Given a string and an integer number n. Remove characters from starting zero up to n and return new string
kp_string = "kartik"
n=3
for i in range(3,len(kp_string)):
    print(string[i])

#6. Given list of numbers iterate and print only those are divisible by 5
new_list = [10,20,33,46,55,70]
for i in range(0,len(new_list)):
    if (new_list[i] % 5 == 0):
        print(new_list[i])

#7. Return count of Kartik in given string
string = input("Enter some text: ")
dict = {}
for i in string:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i] = dict[i] + 1
most_occurring_character = max(dict,key=dict.get)
print("The most occurring character is: ", most_occurring_character)
print("It is repeated %d times" %(dict[most_occurring_character]))

#8. Given list of two numbers create new list such that new list should contain only odd numbers from first list and even numbers from second list
list1 = [10,20,23,11,17]
list2 = [13,43,24,36,12]
final_list_odd = []
final_list_even = []
for i in list1:
    if (i % 2 != 0):
        print(i)
        final_list_odd.append(i)
for x in list2:
    if (x % 2 == 0):
        print(x)
        final_list_even.append(x)
final_list = final_list_odd+final_list_even
print(final_list)

#9. Write a code to extract each digit from an integer, in the reverse order
#-> If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
num = 12345
while num > 0:
    a = num%10 #%
    num = num//10 #1234
    print(a, end= " ")

#10. Print multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")