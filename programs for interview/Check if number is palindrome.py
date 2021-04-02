num = int(input("enter the number: "))
sum=0
temp=num
while(temp>0):
    a = temp%10
    temp = temp//10
    sum = a + (sum*10)
if sum == num:
    print("The number is palindrome number")
else:
    print("The number is not palindrome")