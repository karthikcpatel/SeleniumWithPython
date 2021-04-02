string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if (sorted(string1) == sorted(string2)):
    print("Both strings are anagrams of each other")
else:
    print("Both strings are not anagrams of each other")