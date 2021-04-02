str1 = "Kartik";
str2 = "Patel";
print("Strings before swapping: " + str1 + " " + str2)
str1 = str1 + str2
str2 = str1[0: (len(str1) - len(str2))]
str1 = str1[len(str2):]
print("Strings after swapping: " + str1 + " " + str2)