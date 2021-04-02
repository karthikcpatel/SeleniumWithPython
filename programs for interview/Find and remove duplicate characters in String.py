string = "Hippopotamus".lower()
char = []
for i in string:
    if i not in char:
        char.append(i)
    else:
        print(f"The word {i} appears more than once in the string")
print("String after removing duplicate characters is: ",char)


string = "Hippopotamus".lower()
duplicate = ""
for i in string:
    if i not in duplicate:
        duplicate = duplicate+i
print(duplicate)