array = [10,15,10,16,19,10,15]
temp_array = []
for i in array:
    if array.count(i)>1:
        temp_array.append(i)
print(temp_array)
print("***************")
kpdict = {}
for x in temp_array:
    if x not in kpdict.keys():
        kpdict[x]=1
    else:
        kpdict[x]=kpdict[x]+1
print(kpdict)