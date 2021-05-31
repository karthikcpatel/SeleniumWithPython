#1. Given a string of 7 characters, return three characters in the middle
#2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
string1 = "Kartik"
string2 = "Patel"
middle_index = int(len(string1)//2)

new_string = string1[:middle_index:]+string2+string1[middle_index:]
print(new_string)
#3. Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
str1 = "Kartik"
str2 = "Patel"

first_str1 = str1[0]
middle_str2 = int(len(str1)//2)
first_str2 = str2[0]
last_str2 = int(len(str2)//2)

final_string = first_str1 + first_str2 + str1[middle_str2] + str2[last_str2:]
print(final_string)

#4. Arrange string characters such that lowercase letters should come first
str1 = "KartTiK"
lower = []
upper = []
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
sorted_string = "".join(lower + upper)
print("Arranging characters giving precedence to lowercase letters: ")
print(sorted_string)

#5. Count all lower case, upper case, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
charCount = 0
digitCount = 0
symbolCount = 0
for i in str1:
    if i.islower() or i.isupper():
        charCount+=1
    elif i.isdigit():
        digitCount+=1
    else:
        symbolCount+=1
print("Chars = ",charCount)
print("Digits = ",digitCount)
print("Symbol = ", symbolCount)

#6. Check if one string is present in another string or not
s1 = "Yn"
s2 = "PYnative"
# The output should be True
s1 = "Yn"
s2 = "PYnative"
if s1 in s2:
    print("True")
else:
    print("False")

#7. Find all occurrences of “USA” in a given string ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?".lower()
word = "usa"
print(str1.count(word))

#8. Given an input string, count occurrences of all characters within a string
str1 = "Apple"
#{'A': 1, 'p': 2, 'l': 1, 'e': 1}
str1 = "Apple"
dict = {}
for x in str1:
    if x not in dict.items():
        dict[x] = 1
    else:
        dict[x] = dict[x]+1
print(dict)

#9. Split a given string on hyphens into several substrings and display each substring
str1 = "Kartik is a software engineer"
#Ouput
#Kartik
#is
#a
#software
#engineer
list = str1.split(" ")
print(list)
for x in list:
    print(x)

#10. Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
while("" in str_list) :
    str_list.remove("")

print("After removing empty strings")
print(str_list)

#11. Remove all special characters and digits from string
string = "Hello$@& Python3$"
import re
newstring = re.sub("[$@&3]","",string)
print(newstring)

#12. Removal all the characters other than integers from a string
str1 = 'I am 25 years and 10 months old'
#Output: 2510
list = []
temp_str = ""
for x in str1:
    if x.isdigit():
        obj = "".join(x)
        list.append(obj)
print(list)
for x in list:
    temp_str = temp_str + x
print(temp_str)
