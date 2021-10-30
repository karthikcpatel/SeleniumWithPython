num = int(input("Enter the number: "))
while(num>0):
    a=num%10
    if a!=0 and a!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary")