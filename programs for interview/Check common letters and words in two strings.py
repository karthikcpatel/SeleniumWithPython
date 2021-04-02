str1 = "my name is Kartik"
str2 = "my company is Google"
common_letters=set(str1)&set(str2)
print("The common letters are: ", common_letters)

str1 = "my name is Kartik"
str2 = "my company is Google"
str1_words = set(str1.split(" "))
str2_words = set(str2.split())

common_words = set(str1_words)&set(str2_words)
print("The common words in string are: ",common_words)