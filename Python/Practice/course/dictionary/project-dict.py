#--------------Simple word dictionary project----------------#
dictionary = {
    "dictionary": "A data structure that stores key-value pairs.",
    "list": "A collection of ordered items that can be changed.",
    "tuple": "An ordered collection of items that cannot be changed.",
    "set": "An unordered collection of unique items.",
    "look up":"To search for information about a word or term."
}

# dictionary = dict(
#     dictionary="A data structure that stores key-value pairs.",
#     list="A collection of ordered items that can be changed.",
#     tuple="An ordered collection of items that cannot be changed.",
#     set="An unordered collection of unique items.",
#     look_up="To search for information about a word or term."
# ) 

print("Welcome to the Simple Word Dictionary!\n\n")
word = input(f"Enter a word to look up its meaning: ").lower()

#lookup the word in the dictionary
if word in dictionary:
    print(f"The meaning of '{word}' is: '{dictionary[word]}'")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")
    