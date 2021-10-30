# The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.

sentence1 = "Karti&*k #Pate,l"
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?',;.&*#":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    avg_word = sum(map(len, words)) / len(words)
    return avg_word

print(solution(sentence1))
print(solution(sentence2))