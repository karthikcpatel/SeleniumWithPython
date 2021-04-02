# To initialize a set
kpset = {"one","two","three"}
print(kpset)

# Loop through a set
kpsetnew = {"first","second","third"}
for x in kpsetnew:
    print(x)

# Add elements to a set
kpsetnew.add("Added")
print(kpsetnew)

# Removing an element using remove. An error will be raised if element is not present
kpsetnew.remove("second")
print(kpsetnew)

# Removing an element using discard
kpsetnew.discard("first")
print(kpsetnew)

# Add any iterable to set using update
set1 = {"one","two","three"}
tuple = ("four","five")
set1.update(tuple)
print(set1)

set2 = {"one","two","three"}
list = ["four","five"]
set2.update(list)
print(set2)

# This method will return elements present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# This method will return elements not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

