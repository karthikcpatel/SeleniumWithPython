i=1
while (i<5):
    print(i)
    i = i+1
print("*********")

# Using break to break loop execution
i=1
while(i<5):
    print(i)
    break
    i = i+1
print("*********")

# Using continue to skip current loop execution
i=1
while(i<5):
    i = i + 1
    if i == 3:
        continue
    print(i)

# Using while-else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")