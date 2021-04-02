string = "aaaabbbcccd"
previous = string[0]
output = ""
count=1
i=1
while i<len(string):
    if string[i]==previous:
        count=count+1
    else:
        output = output + str(count)+previous
        previous = string[i]
        count=1
    if i==string[-1]:
        output = output+str(count)+previous
    i=i+1
print(output)