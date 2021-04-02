string = input("Enter a sentence separated by comma: ")
list = string.split(" ")
dict = {}
for i in list:
    if i not in dict.keys():
        dict[i]=0
    dict[i]=dict[i]+1
print(dict)