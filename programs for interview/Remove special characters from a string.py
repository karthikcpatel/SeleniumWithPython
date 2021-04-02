string = "Hello$@& Python3$"
import re
newstring = re.sub("[$@&3]","",string)
print(newstring)

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = " ".join(weekdays)
print(listAsString)

