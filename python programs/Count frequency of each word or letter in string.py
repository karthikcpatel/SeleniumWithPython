string = "My name is Kartik. My home town is Navsari"
list = string.split(" ")
dict = {}
for i in list:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print("Count of all letters in given string is:\n" , dict)
most_occurring_character = max(dict,key=dict.get)
print("The most occurring word is: ", most_occurring_character)
print("It is repeated %d times" %(dict[most_occurring_character]))

test_str = "hippopotamus"
empty_dict = {}
for i in test_str:
    if i not in empty_dict.keys():
        empty_dict[i] = 1
    else:
        empty_dict[i] = empty_dict[i]+1

print("Count of all characters in given string is:\n ", empty_dict)
most_occurring_character = max(empty_dict,key=empty_dict.get)
print("The most occurring word is: ", most_occurring_character)
print("******************************")
for k, v in empty_dict.items():
    print(f'Character {k} occurs {v} appears times'.format(k, v))

