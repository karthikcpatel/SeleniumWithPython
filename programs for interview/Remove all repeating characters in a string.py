string = input("Enter the word: ").lower()
remove_duplicate = ""
count = 0
for i in string:
    if string.count(i)>1:
        pass
        #count = count + 1
        #print(f"The character {i} is repeated {count} times")
    elif string.count(i)==1:
        remove_duplicate = remove_duplicate + i
    else:
        print("There are no non-repeating characters in given string")
print(remove_duplicate)
