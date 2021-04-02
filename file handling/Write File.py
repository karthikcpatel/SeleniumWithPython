#append content to a file
file = open("C:\\Users\\kartikp\\Downloads\\kp.txt", "a")
file.write("Now the file has more content!")
file.close()

#overwrite content in file
file = open("C:\\Users\\kartikp\\Downloads\\kp.txt", "w")
file.write("Woops! I have deleted the content!")
file.close()