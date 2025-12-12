dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}
dict2 = {
    "a": 20,    
    "d": 30,
    "e": 40,
    "f": 50
}
# Merging two dictionaries
# dict1.update(dict2)
# print(f"Merged dictionary is: {dict1}")
# dict2.update(dict1)
# print(f"Merged dictionary 2 is: {dict2}")

# merged_dict = {**dict1, **dict2}
merged_dict = {**dict2, **dict1}
print(f"Dict1 is: {dict1}")
print(f"Dict2 is: {dict2}")
print(f"Merged dictionary using ** is: {merged_dict}")