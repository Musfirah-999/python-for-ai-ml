person = {
    "firstname": "John",
    "lastname": "Doe",
    "age": 25,
    "jobs": ["Developer", "Manager"],
    # "job": "Programmer",
}

print(f"Type of person is {type(person)}")
print(f"The person is {person}")

# person.pop("jobs")  # Removing key-value pair using pop
# print(f"The person after pop is {person}")

# person["points"] = 10.0  # Adding new key-value pair
# print(f"The person after adding points is {person}")

# person.popitem()  # Removing the last inserted key-value pair using popitem
# print(f"The person after popitem is {person}")

# del person["lastname"]  # Removing key-value pair using del
# print(f"The person after del is {person}")

# del person
# # print(person)  # This will raise an error since person is deleted
# print("Person dictionary is deleted.")

# person.clear()  # Removing all key-value pairs using clear
# print(f"The person after clear is {person}")