#1. Reverse a list in Python
#2.Expected output - ['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
lis4 = list(zip(list1, list2))
print(list3)
print(lis4)
list4 = zip(list1,list2)
#3. Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)
#4. Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for x in list1:
    for y in list2:
        print(x+y)
resList = [x+y for x in list1 for y in list2]
print(resList)

#4. Given a two Python list.
# Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
#Expected output - 10 400
# 20 300
# 30 200
# 40 100
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

#5. Remove empty strings from list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for x in list1:
    if "" in list1:
        list1.remove("")
print(list1)

#6. Add items 7000 after 6000 in following Python list:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#7. Remove duplicate elements from list
list1 = [5, 20, 15, 20, 25, 50, 20]
removed = []
for i in list1:
    count = list1.count(i)
    if list1.count(i)==1:
        removed.append(i)
    elif list1.count(i)>1:
        pass
list1 = removed
print("The list after removing duplicate elements are: ",list1)

#8. Replace first 20 with 200 in given list
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#9. Remove more than one occurance of a value from string in pyton
list1 = [5, 10, 15, 20, 25, 50, 20]
for i, item in enumerate(list1):
    if item == 20:
        list[i] = 200
        break

print (list1)

#10. Add elements to a list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)