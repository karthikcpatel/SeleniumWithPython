def arePairs(open,close):
    if open=='[' and close==']':
        return True
    if open=='{' and close=='}':
        return True
    if open=='(' and close==')':
        return True
    return False

def Balanced(string):
    stack=[]
    for i in range(len(string)):
        if string[i]=='[' or string[i]=='{' or string[i]=='(':
            stack.append(string[i])
        elif string[i] == ']' or string[i] == '}' or string[i] == ')':
            if arePairs(stack[-1],string[i] or len(stack)!=0):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

string="[()]{}{[()()]()}"
print(Balanced(string))