# people = {
#     # "count": 2,
#     "person1": {
#         "name": "Alice",
#         "age": 30,
#         "city": "New York"
#     },
#     "person2": {
#         "name": "Bob",
#         "age": 25,
#         "city": "Los Angeles"
#     },
# }

person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
person2 = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
people = {
    "person1": person1,
    "person2": person2,
}

print(f"People is {people}")
print(f"Person 1 is {people['person1']}")
print(f"Person1 name is: {people['person1']['name']}")

for k, items in people.items():
    print(f"Key: {k} => Value: {items}")
