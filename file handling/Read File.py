#open() method returns file object.
#read() method is used for reading content of file.
file = open(r"C:\Users\kartik.patel\Downloads\kp.txt","r")
print(file.read())
file.close()

#read some parts of file
file = open(r"C:\Users\kartik.patel\Downloads\kp.txt","r")
print(file.read(500))
file.close()

#read one line by using readLine() method
file = open(r"C:\Users\kartik.patel\Downloads\kp.txt","r")
print(file.readline())
file.close()

#loop through
file = open(r"C:\Users\kartik.patel\Downloads\kp.txt","r")
for x in file:
    print(x)
file.close()