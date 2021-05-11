string = "Hello$@& Python3$"
import re
newstring = re.sub("[$@&3]","",string)
print(newstring)


