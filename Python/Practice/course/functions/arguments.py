# Variable Length Arguments (*args)
def showValues(*args):
    for items in args:
        print(items," ", end="")
# # showValues(1, 2, 3, 4)
# # showValues("apple", "banana", "cherry")
# showValues(1, "apple", 3.14, True)


def showKeywordValues(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# showKeywordValues(name="Alice", age=30, city="New York")
# showKeywordValues()

def showMixed(*args, **kwargs):   #args is considered as tuple and kwargs as dictionary
    print("----args----")
    for items in args:
        print(items," ", end="")
    print()  # for new line
    print("----kwargs----")
    for k, v in kwargs.items():
        print(f"{k}: {v}")
# showMixed(1, 2, 3, name="Alice", age=30)
showMixed(1,2,3, name="Bob", country="USA")