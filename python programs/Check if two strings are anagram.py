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

### Approach 3. Building logic ###

def check_anagram(data1, data2):
    flag = False
    if (len(data1) == len(data2)):
        if (set(data1.lower()) == set(data2.lower())):
            for i in range(len(data1)):
                if data1[i] != data2[i]:
                    flag = True

    return flag

print(check_anagram("Silent", "Listen"))