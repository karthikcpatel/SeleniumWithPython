# There is a lot of work in building an iterator in Python
# We have to implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.
# This is both lengthy and counter intuitive. Generator comes to the rescue in such situations.
# Generator function contains one or more yield statements.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next()
# Finally, when the function terminates, StopIteration is raised automatically on further calls

# https://herovired.com/learning-hub/blogs/generators-in-python/

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

for item in my_gen():
    print(item)

print("*************************")

def square_of_sequence(x):
    for i in range(x):
        yield i*i

gen=square_of_sequence(5)
while True:
    try:
        print ("Received on next(): ", next(gen))
    except StopIteration:
        break

squres = square_of_sequence(5)
for sqr in squres:
    print(sqr)