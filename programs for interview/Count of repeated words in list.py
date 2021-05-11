#list = ["a", "b", "a", "c", "c", "a", "c"]
list = [1, 2, 1, 2, 3, 4, 5]
temp=set(list)
result={}
for i in temp:
    result[i]=list.count(i)
print (result)