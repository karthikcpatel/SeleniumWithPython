# Python program to illustrate functions
# can be passed as arguments to other functions
# Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)