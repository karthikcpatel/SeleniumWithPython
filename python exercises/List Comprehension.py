# Generate a list of squares for numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]

# Create a list of all even numbers from 1 to 20.
even_numbers = [print(x) for x in range(1,21) if x%2==0]

# Given a list of words, generate a new list containing the length of each word.
word_lengths = [len(word) for word in ["apple", "banana", "cherry"]]

# Convert a list of strings to uppercase.
string = ["hello", "world"]
uppercase_strings = [print(string.upper()) for string in ["hello", "world"]]

# Create a list of squares for only the odd numbers from 1 to 10.

# Extract all vowels from a given string.

# Generate all prime numbers less than 50 using list comprehension.
primes = [print(x) for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

# Replace all even numbers in a list with "Even" and all odd numbers with "Odd".
#Multiples of 3 or 5
multiples = [print(x) for x in range(1, 51) if x % 3 == 0 or x % 5 == 0]

