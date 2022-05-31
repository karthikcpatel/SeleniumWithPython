string = "Hippopotamus".lower()
char = []
for i in string:
    if i not in char:
        char.append(i)
    else:
        print(f"The word {i} appears times", string.count(i))
print("String after removing duplicate characters is: ",char)


string = "Hippopotamus".lower()
duplicate = ""
for i in string:
    print(f"The word {i} appears times", string.count(i))
    if i not in duplicate:
        duplicate = duplicate+i
    else:
        pass
print(duplicate)