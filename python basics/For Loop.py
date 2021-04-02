# Print elements in a list using for loop
name = ["Kartik","Dipika","Bhavyesh","Doshi"]
for x in name:
    print(x)

# Print 1 to 5 using for loop
for numbers in range(1,6,1):
    print(numbers)

# Nested for loop
adj = ["Kartik", "Dipika"]
fruits = ["Patel", "Patil"]

for x in adj:
  for y in fruits:
    print(x, y)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")

string_name = "kartik"
for kp in range(0, len(string_name)):
    print(string_name[kp])
