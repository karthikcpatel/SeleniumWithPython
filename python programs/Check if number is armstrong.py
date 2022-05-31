def check_armstrong(num):
    temp = num
    sum = 0
    while (temp>0):
        a = temp%10
        temp = temp//10
        sum = sum + (a*a*a)
    if sum == num:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")

check_armstrong(153)