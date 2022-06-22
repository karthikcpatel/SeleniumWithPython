sentence = input("Enter the sentence whose words we want to reverse: ")
list_of_words = sentence.split(" ") #
print(list_of_words) #['bhavesh','amit','kartik','vimal', ashwini]
reversed_list = list_of_words[::-1]
print(reversed_list)
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)


sentence = input("Enter the sentence whose each words we want to reverse: ")
for reversed_word in sentence.split(" "):
    print(reversed_word[::-1],end=' '"\n")

sentence_other = "kartik patel my"
print(sentence_other[::-1], end=' ')