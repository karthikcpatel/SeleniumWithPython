string = "aabbccdaa"
new_string = ""
count = 1
for i in range(0,len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:
        new_string =  new_string + string[i] + str(count)
        count = 1
new_string = new_string + string[i+1] + str(count)
print(new_string)
