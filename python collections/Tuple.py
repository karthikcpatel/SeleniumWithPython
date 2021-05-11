# Initializing a tuple
kptuple = ("kartik","bhavyesh","dipika")
print(kptuple)

# Check if a value is present in a tuple
tupnew = ("kartik","patel")
if "kartik" in kptuple:
    print("Yes. Kartik is present")

# Loop through a tuple
for x in kptuple:
    print(x)

# Copy a tuple to other tuple
tup1 = ("one","two")
tup2 = ("three","four")

# Tuple can contain any data
tuple1 = (1,"Kartik",5.0)
print(tuple1)

# Add elements in tuple by converting it to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Join tuple using + operator
tup1 = (1,2,3)
tup2 = ("one","two","three")
tup = tup1 + tup2
print(tup)

# Join two tuples using zip operator
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))

# Create a tuple using tuple constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Lists inside tuple
complex_tuple = ([1,2],[3,4],[5,6])
for i in complex_tuple:
    for j in i:
        print(j)

# Unpack a tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Add dictionary to a tuple
test_tup = (4, 5, 6)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize dictionary
test_dict = {"gfg": 1, "is": 2, "best": 3}

# Add dictionary to tuple using + operator
res = test_tup + (test_dict,)

# printing result
print("Tuple after addition of dictionary : " + str(res))