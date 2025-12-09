word_count = {}

with open("data.txt", "r") as file:
    text = file.read()
    words = text.split()   

    for word in words:
        # increment count if word exists, else start at 1
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)



''' method -2'''
'''
sentence = "the quick brown fox jumps over the lazy dog and the quick blue hare"
for word in sentence.split():
    word = word.lower().strip(".,!?")
    if word not in word_coun:
        word_coun[word] = 1
    else:
        word_coun[word] += 1
'''
