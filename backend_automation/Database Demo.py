from AllPayloads import *
#from utilities.configurations import *
import mysql.connector

connection = mysql.connector.connect(host = 'localhost', database = 'APIDevelop', user = 'root', password = 'root')
#connection = get_connection()
cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
for row in rows:
    print(row)
    if "Jmeter" in row:
        print("It is present")

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query,data)

connection.close()