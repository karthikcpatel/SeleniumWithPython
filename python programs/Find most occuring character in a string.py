string = input("Enter some text: ")
dict = {}
for i in string:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i] = dict[i] + 1
print(dict)
most_occurring_character = max(dict,key=dict.get)
print("The most occurring character is: ", most_occurring_character)
print("It is repeated %d times" %(dict[most_occurring_character]))