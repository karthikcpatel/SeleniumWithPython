#1. Accept two numbers from user and calculate the addition of those two numbers.
#2. Display "My name is Kartik" as "My**name**is**Kartik"
string = "My name is Kartik"
print("My","name","is","Kartik",sep="**")
#3. Display float number with 2 decimal places using print()
print("%.2f" %458.5432234)
#4. Accept a list of floating numbers from user
#5. Accept any three string from one input() call
str1, str2, str3 = input("Enter three string: ").split()
print(str1, str2, str3)
#6. Format the given string
#-> I have 1000 dollars so I can buy 3 football for 450.00 dollars.
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))