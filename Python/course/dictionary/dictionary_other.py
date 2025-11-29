person = {
    "firstname": "John",
    "lastname": "Doe",
    "age": 25,
    "jobs": ["Developer", "Manager"],
    # "job": "Programmer",
}

print(f"Type of person is {type(person)}")
print(f"The person is {person}")

# person.update({"age": 26, "lastname": "Smith"})  # Updating existing key-value pairs
# person2 = person   #shallow copy
# print(f"The person2 is {person2}")

# person2["firstname"] = "Jane"
# print(f"The person is {person}")
# print(f"The person2 is {person2}")

# person2 = person.copy()   #deep copy
# print(f"The person2 is {person2}")
# person["firstname"] = "Jane"
# print(f"The person is {person}")    
# print(f"The person2 is {person2}")

# person2 = dict(person)   #deep copy
# print(f"The person2 is {person2}")
# person["firstname"] = "Jane"    
# print(f"The person is {person}")
# print(f"The person2 is {person2}")

# person.items()  # Returns a view object that displays a list of a dictionary's key-value tuple pairs
# print(f"Person's all items are {person.items()}\n\n")

# person["age"] = 26  # Updating existing key-value pair
# print(f"The person after updating age is {person}")

# person.update({"age": 26, "lastname": "Smith", "Height" : 170})  # Updating existing key-value pairs
# print(f"The person after update is {person}")

# if person["age"] > 18:
#     print("Person is an adult.")
# else:
#     print("Person is a minor.")

# if person["hair_color"] == "black":
#     print("Person has black hair.")   #This will raise an error since "hair_color" key does not exist
# else:
#     print("Person's hair color is not black.")

# print(f"using a keyname that is not present in the dictionary: {person.get('hair_color', 'blue')}")

print(f"Checking if a key exists in the dictionary:")
if "age" in person:
    print("Age key is present in the person dictionary.")
else:
    print("Age key is not present in the person dictionary.")
    
person.pop("age")  # Removing key-value pair using pop