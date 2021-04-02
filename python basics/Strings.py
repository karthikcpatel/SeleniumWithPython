# In Python, both single quote and double quote are valid.
print('Hello')

# Assigning String to a variable
name = "Kartik"
print(name)

# Escape characters in a string
txt = "We are the so-called \"Viking's\" from the north."
print(txt)

# Multi line strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Access elements in string
new = "Hello World!"
print(new[2])

# Loop through a string
string_loop = "String"
for x in string_loop:
    print(x)

# Get length of a string
string_length = "Kartik"
print(len(string_length))

# Check if word is present in a string
check_string = "My name is Kartik"
print("Kartik" in check_string)

# We can also access elements in string using slicing
string_slicing = "Kartik"
print(string_slicing[1:5]) #for this case 1 will be included and 5 will be ignored
print(string_slicing[-4:-1]) #for this case -1 will be last k

# Converting string to uppercase
string_upper = "Kartik"
print(string_upper.upper())

# Converting string to lowercase
string_lower = "Kartik"
print(string_lower.lower())

# Remove whitespace
string_remove_whitespace = " Hello Everyone "
print(string_remove_whitespace.strip())

# Replace words in string
string_replace = "Hello Everyone...."
print(string_replace.replace(".","!"))

# Replace more than one words in string
kp_string = "kartikpatel"
remove_characters = ["k","e","l"]

for character in remove_characters:
    kp_string = kp_string.replace(character, "")

print(kp_string)

# The split() method splits the string into substrings if it finds instances of the separator
string_split = "Hello, All!"
print(string_split.split(","))

# To combine two strings + operator is used
string_one = "Kartik"
string_two = "Patel"
string_final = string_one+string_two
print(string_final)

# String format. If we want to add numbers in a string
age = 30
string = "My name is Kartik, and my age is {}"
print(string.format(age))

company = "Amazon"
name = "Kartik"
age = 30
final_string = "My name is {1} having age {2}. I work for {0}"
print(final_string.format(company,name,age))

# count method to return occurrence of word in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# finds first occurrence of specified value
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# joins all items of a tuple into a string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Join all keys of a dictionary
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)