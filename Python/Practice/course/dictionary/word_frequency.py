sentence = input("Enter a sentence: ").lower().split()

word_count = {

}
for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1

# print(f"Word frequency dictionary: {word_count}")

for word, count in word_count.items():
    print(f"{word}: {count}")

    # how many times a character appears in whole sentence
char_count = {}
for char in "".join(sentence):
    char_count[char] = char_count.get(char, 0) + 1
for char, count in char_count.items():
    print(f"'{char}': {count}")
