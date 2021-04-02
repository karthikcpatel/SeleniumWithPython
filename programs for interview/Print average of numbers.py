n = int(input("Enter number of elements to be inserted: "))
a = []
for i in range(0,n):
    elements = int(input("Enter the elements: "))
    a.append(elements)
    avg = sum(a)//n
print("The average of numbers is: ",+avg)