#1. Acces value 20 from following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
#Output: 20

#2. Create a tuple with single item 50
kptuple = (50,)
print(kptuple)

#3. Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
(a,b,c,d) = aTuple
print(a)
print(b)
print(c)
print(d)

#4. Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple_temp = tuple1[3:5]
print(tuple_temp)

#5. Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0]=222
tuple_new = tuple(list1)
print(tuple_new)

#6. Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
for x in tuple1:
    if tuple1[0]==x:
        print("All of them are same")
    else:
        print("All of them are not same")

#7. Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
occurance = tuple1.count(50)
print(occurance)