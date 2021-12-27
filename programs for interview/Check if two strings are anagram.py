### Approch 1. Using sorted function ###

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if (sorted(string1) == sorted(string2)):
    print("Both strings are anagrams of each other")
else:
    print("Both strings are not anagrams of each other")

### Approach 2. Using set function ###

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if set(string1.lower()) == set(string2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")