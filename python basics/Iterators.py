# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
# The iterator object is initialized using the iter() method.
# It uses the next() method for iteration.
# Iterators allow lazy evaluation, only generating the next element of an iterable object when requested
# It saves CPU memory and RAM.

# Here is an example of a python inbuilt iterator
# value can be anything which can b
# e iterate
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)

while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        # exception will happen when iteration will over
        break