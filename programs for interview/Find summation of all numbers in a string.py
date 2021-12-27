string = "12abc20yz68"
temp = "0"
sum = 0

for ch in string:
    if (ch.isdigit()):
        temp = temp + ch
    else:
        sum = sum + int(temp)
        temp = "0"
print(sum+int(temp))