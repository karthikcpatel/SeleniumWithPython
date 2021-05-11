string = input("Enter a sentence separated by space: ")
list = string.split(" ")
dict = {}
for i in list:
    if i not in dict.keys():
        dict[i]=0
    dict[i]=dict[i]+1
print("Count of all letters in given string is:\n" , dict)

test_str = "kartikpatel"
empty_dict = {}
for i in test_str:
    if i in empty_dict.keys():
        empty_dict[i] = empty_dict[i]+1
    else:
        empty_dict[i] = 1

print("Count of all characters in given string is:\n " + str(empty_dict))