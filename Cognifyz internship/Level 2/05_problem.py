# File Manipulation
file = open("sample.txt", "r")
text = file.read()
file.close()

words = text.lower().split()
word_count = {}
for word in words:
    word = word.strip(".,!;:()[]{}")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Occurences : \n")

for word in sorted(word_count):
    print(f"{word} : {word_count[word]}")