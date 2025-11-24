word_count = {}

with open("data.txt", "r") as file:
    text = file.read()
    words = text.split()   

    for word in words:
        # increment count if word exists, else start at 1
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)
