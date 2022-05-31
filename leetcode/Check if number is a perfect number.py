num = int(input("please give first number a: "))
sum=0
for i in range(1,num):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num:
    print("The given no is perfect number")
else:
    print("The given no is not a perfect number")