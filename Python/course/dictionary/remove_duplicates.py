my_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
}
print(f"Original dictionary: {my_dict}")

new_dict = {}
for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(f"New Dictionary : {new_dict}")
# Removing duplicates
