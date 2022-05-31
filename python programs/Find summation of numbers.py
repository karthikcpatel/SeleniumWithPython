number = int(input("Enter a number: "))
total=0
while(number>0):
    a=number%10#6
    number=number//10
    total=total+a
print("The summation is ",total)