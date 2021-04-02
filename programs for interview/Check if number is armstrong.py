num = int(input("enter the number: "))
sum=0
temp=num
while(temp>0):
    a = temp%10
    temp = temp // 10
    sum = sum+(a**3)
if num==sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")