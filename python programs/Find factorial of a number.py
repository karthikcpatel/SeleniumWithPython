num = int(input("Enter the number to calculate the factorial: "))
fact = 1
if num<0:
    print("The factorial of a negative number is not possible")
elif num==0:
    print("The factorial of 0 is not possible")
else:
    for i in range(1,num+1):
        fact = fact*i
print("The factorial of",num,"is",fact)