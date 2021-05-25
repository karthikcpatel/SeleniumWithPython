#1. Given a string of 7 characters, return three characters in the middle
#2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
str1 = "Kartik"
str2 = "Patel"
iddleIndex = int(len(str1) /2)
#3. Arrange string characters such that lowercase letters should come first
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
#4. Count all lower case, upper case, digits, and special symbols from a given string
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
#5.