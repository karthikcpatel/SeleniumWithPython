# Else block will be printed if it is present after for and while loop
# Break will terminate the loop
print("Kartik",sep='&')

print("",sep='--')

print("one",end=',')
print("",sep="!!")

a=21
b=10
c=a/b
print(c)
d=a//b
print(d)
e=a%b
print(e)

#Below is a tuple
thistuple = ("apple",)
print(type(thistuple))

#Below is a string and not a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print(("Repeat"*3,) * 3)

listtostring = ["ahm","pune","hyd"]
str = ",".join(listtostring)
print(str)

pow2 = [2 ** x for x in range(10)]
print(pow2)

print(range(10))

student_name = 'Jules'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')

digits = [1, 2, 3]
for i in digits:
    print(i)
    break
else:
    print("No items left.")

for val in "string":
    if val == "i":
        break
    print(val)
else:
    print("The end")
print(val)

dict1 = {"John":1234, "Fruit":"Apples"}
dict2 = {"Fruit":"Apples", "John":1234}
print(dict1 == dict2)
print(dict1 is dict2)

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
list3 = [1,2,3,4,5]
print(list1 == list2)
print(list1 is list2)
print(list1 == list3)
print(list1 is list3)

str1 = "String"
str2 = "String"
print(str1 is str2)
print(str1 == str2)

ui_elements = dict([('radio_button', 2),('text_box', 3),('standard_button', 5)])
popped_element = ui_elements.popitem()
print(list(popped_element))

ui_elements = dict([('radio_button', 2),('text_box', 3),('standard_button', 5)])
ui_elements.popitem()
print(ui_elements)

def fun(x):
    return ["Tea"]
coffees = ["Cappuccino","Latte","Macchiato"]
x = fun(coffees)
print(x)

milk_left = ""
if milk_left:
    print("Groceries trip pending!")
else:
    print("Let's enjoy a bowl of cereals")

milk_left = "None"
if milk_left:
    print("Groceries trip pending!")
else:
    print("Let's enjoy a bowl of cereals")

val1 = 0b111
val2 = val1 << 2

capitals1 = ["London","New York","Rome"]
capitals2 = capitals1
capitals2.remove("New York")
print(capitals1)

print("red roses and violet roses")
print(" Kartik's roses and 'violet' roses")
print("""red roses and violet roses""")

tupA = (2, 6, 8, 9)
tupB = (4, 6, 7)
tupC = (6, 5, 2, 1)
tupA = (tupA + tupB + tupC)
print(tupA)

if 1:
    print("1 will be printed")
else:
    print("???")

if False:
    print("Nissan")
elif True:
    print("Ford")
elif True:
    print("BMW")
else:
    print("Audi")

if not True:
    print("True")
else:
    print("False")

raw_str = r"raw \n string"
print(raw_str)

multiline_str = """This is a multiline string with more than one line code."""
print(multiline_str)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

pow2 = [2 ** x for x in range(10)]
print(pow2)