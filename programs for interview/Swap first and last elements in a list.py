num = int(input("Enter total number of elements in list: "))
list = []
for i in range(0,num):
    elements = int(input("Enter each elements of a list: "))
    list.append(elements)
print("The list before swapping first and last values is ", list)

temp = list[0]
list[0]=list[-1]
list[-1]=temp
print("The list after swapping first and last values is ", list)

# Without using third or temp variable, it can be done as below:
# newList[0], newList[-1] = newList[-1], newList[0]