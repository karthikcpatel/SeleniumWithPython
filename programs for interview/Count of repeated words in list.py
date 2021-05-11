list = ["a", "b", "a", "c", "c", "a", "c"]
temp=set(list)
result={}
for i in temp:
    result[i]=list.count(i)
print (result)