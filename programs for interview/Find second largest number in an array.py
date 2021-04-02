list = []

n = int(input("Enter length of list: "))
for i in range(0,n):
    elements = int(input("Enter number of elements: "))
    list.append(elements)
print(list)

list.sort(reverse=True)
print(list)
print(list[1])
