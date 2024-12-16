# Print a list
kplist = ["Kartik","Chetan","Nikhil"]
print(kplist)

# Loop through a list
for x in kplist:
    print(x)

# Loop through by using their index
for i in range(len(kplist)):
    print(kplist[i])

# Access element in a list
print(kplist[2])

# List can contain any type of values
mixed_list = [1,"Kartik", 5.0,3+4j]
print(mixed_list)

# Add elements to a list
kplist_add = ["First","Second","Third","Fourth"]
kplist_add.append("Sixth")
print(kplist_add)

kplist_1 = [1,2,3,4]
kplist_2 = [5,6,7]
kplist_1.append(kplist_2)
print(kplist_1)

kplist_1 = [1,2,3,4]
kplist_2 = [5,6,7]
kplist_1.extend(kplist_2)
print(kplist_1)

# Insert elements in list using index position
kplist_insert = ["One","Two","Three"]
kplist_insert.insert(3,"Four")
print(kplist_insert)

# Add any iterable to a list using extend
newlist = ["One","Two"]
newtuple = ("Three","Four")
newlist.extend(newtuple)
print(newlist)

# Update elements in a list
kplist[1]="Chetan"
print(kplist)

# Update multiple values in a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Clear values in a list
kplist_clear = ["Test1","Test2","Test3"]
kplist_clear.clear()
print(kplist_clear)

# To remove an element in a list using index
kplist_insert.pop(1)
print(kplist_insert)

# To remove an element in a list using value
kplist_insert.remove("Three")
print(kplist_insert)

# Sort List
list_sort = [1,22,11,33,10]
list_sort.sort()
print(list_sort)

# Sort List In Reverse
list_sort = [1,22,11,33,10]
list_sort.sort(reverse=True)
print(list_sort)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Copying a list. We cannot directly write list1=list2 as changes made in one list will affect others
# We will use built-in copy() method
first_list = ["First","Second","Third"]
second_list = first_list.copy()
print(second_list)

# Join two lists. We can join two lists using + operator
first_list = ["apple","orange"]
second_list = ["truck","car"]
final_list = first_list + second_list
print(final_list)

# Convert list to string using join method
listtostring = ["ahm","pune","hyd"]
str = ",".join(listtostring)
print(str)
print(type(str))

# Tuple inside list
complex_list = [("one","two"),("three","four")]
for x in complex_list:
    for y in x:
        print(y)

# Dictionary inside list
complex_list = [{"Kartik":"Patel","Chetan":"Patel"}]
for x in complex_list:
    for y in x.items():
        print(y)

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]

kplist_new = ["Kartik","Chetan","Nikhil"]
print(kplist_new[1])