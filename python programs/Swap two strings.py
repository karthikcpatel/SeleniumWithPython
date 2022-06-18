str1 = "Kartik";
str2 = "Patel";
print("Strings before swapping: " +str1+ " " +str2)
str1 = str1 + str2
str2 = str1[0: (len(str1) - len(str2))]
str1 = str1[len(str2):]
print("Strings after swapping: " +str1+ " " +str2)


string1 = "kartik"
string2 = "patel"

string2 = string1+string2
string1 = string2[0: (len(string2) - len(string1))] #kartikpatel-kartik = #patel
print(string1)
string2 = string2[len(string1):]
print(string2)