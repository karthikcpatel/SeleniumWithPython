# If elif else
a = 100
b = 150
if a>b:
    print("A is greater")
elif b>a:
    print("B is greater")
else:
    print("Both are same")

# Using and keyword
a = 100
b = 150
c = 200
if a>b and a>c:
    print("A is the greatest number")
elif b>a and b>c:
    print("B is the greatest number")
else:
    print("C is the greatest number")

# Using nested if
x = 45
if x> 10:
    print("X is above 10")
    if x>20:
        print("X is above 20")
    else:
        print("X is greater than 10 and 20")