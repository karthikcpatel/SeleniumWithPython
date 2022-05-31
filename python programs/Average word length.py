# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

sentence1 = "Karti&*k #Pate,l"
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.&*#":
        sentence = sentence.replace(p, '')
    words = sentence.split(" ")
    print(len(words))
    avg_word = sum(map(len, words)) / len(words)
    print (avg_word)

solution(sentence1)
solution(sentence2)