# First approach using sort method
# list = []
#
# n = int(input("Enter length of list: "))
# for i in range(0,n):
#     elements = int(input("Enter number of elements: "))
#     list.append(elements)
# print(list)
#
# list.sort(reverse=True)
# print(list)
# print(list[1])

# Second approach by removing the max from the list
list1 = [10, 20, 4, 45, 99]

# new_list is a set of list1
new_list = set(list1)

# removing the largest element from temp list
new_list.remove(max(new_list))

# elements in original list are not changed
# print(list1)

print(max(new_list))

# Third approach is using for loop
kplist = [55,1,45,68,159,75,5,14]

def find_second_maximum(list1):
    first_max = max(list1[0],list1[1])
    second_max = min(list1[0],list1[1])

    for i in range(2,len(list1)):
        if list1[i] > first_max:
            second_max = first_max
            first_max = list1[i]

        elif list1[i] > second_max:
            second_max = list1[i]
    return second_max
print("The second maximum number is ", find_second_maximum(kplist))

