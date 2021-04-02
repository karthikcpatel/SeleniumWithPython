list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

#The output of the first if the condition is “True” as both list1 and list2 are empty lists.
#Second, if the condition shows “False” because two empty lists are at different memory locations. Hence list1 and list2 refer to different objects. We can check it with id() function in python which returns the “identity” of an object.
#The output of the third if the condition is “True” as both list1 and list3 are pointing to the same object.
#The output of the fourth if the condition is “False” because the concatenation of two lists always produces a new list.