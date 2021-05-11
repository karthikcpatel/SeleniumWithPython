def check(my_string):
    paranthesis = ['()', '{}', '[]']
    while any(x in my_string for x in paranthesis):
        for para in paranthesis:
            my_string = my_string.replace(para, '')
    return not my_string


# Driver code
string = "{[]{()}}"
print(string, "-", "Balanced"
if check(string) else "Unbalanced")