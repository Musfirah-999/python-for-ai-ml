person = {
    "firstname": "John",
    "lastname": "Doe",
    "age": 25,
    "jobs": ["Developer", "Manager"],
    # "job": "Programmer",
}

print(f"Type of person is {type(person)}")
print(f"The person is {person}")

print("Looping through dictionary keys and values:")
for k in person:
    print(f"{k} : {person[k]}")
print("-----print using key only:")
for k in person.keys():
    print(k)
print("-----print using values only:")
for v in person.values():
    print(v)

print("-----print using items():")
for k, v in person.items():
    print(f"{k} : {v}")