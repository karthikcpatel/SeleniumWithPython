list = ["a", "b", "a", "c", "c", "a", "c"]
result = {}
for i in list:
    result[i] = list.count(i)
print(result)