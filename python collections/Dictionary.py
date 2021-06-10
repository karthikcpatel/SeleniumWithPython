# Initialize a dictionary
kpdict = {"Kartik":"Patel","Bhavyesh":"Patel","Dipika":"Patil"}
print(kpdict)

# Loop through a dictionary
for key,value in kpdict.items():
    print(key,value)

# Fetch a value based on key
x = kpdict['Kartik']
print(x)

# Fetch all keys
x = kpdict.keys()
print(x)

# Fetch all values
x = kpdict.values()
print(x)

# Update a value in a dictionary
kpdict["Kartik"] = ["Shah"]
print(kpdict)

# Update value in dictionary using update method
kpdict = {"Kartik":"Patel","Bhavyesh":"Patel","Dipika":"Patil"}
kpdict_new = {"1":"Updated value"}
kpdict.update(kpdict_new)
print(kpdict_new)

# Remove an item from a key using pop
kpdict.pop("Dipika")
print(kpdict)

# Remove an item from a key using del
del kpdict["Bhavyesh"]
print(kpdict)

# Copy of a dictionary
newkpdict = kpdict.copy()
print(newkpdict)

# Nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)