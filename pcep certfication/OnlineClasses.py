tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0]=222
tuple_new = tuple(list1)
print(tuple_new)