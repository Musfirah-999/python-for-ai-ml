
def congracts(name,prize):
    print(f"Congratulations {name}! You have won {prize}.\n")
congracts(prize="$1000", name="Alice") #keyword parameters
congracts("Bob", prize="a car") #mixed parameters
congracts("Charlie", "a vacation") #positional parameters

def showNumbers(*args):
    # for number in args:
    print(args)
print()
showNumbers(1,2,3,4,5)
showNumbers("apple", "banana", "cherry")
showNumbers(1, "apple", 3.14, True)

def showInfo(**kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    print(kwargs)
print()
showInfo(name="Alice", age=30, city="New York")
showInfo()

person = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
person.pop("age")  # Remove age key-value pair

def positional_only(x,y,/):
    print(f"{x} + {y} = {x+y}")

positional_only(5,10)
# positional_only(x=5, y=10)  # This will raise a TypeError
def keyword_only(*, x, y):
    print(f"{x} * {y} = {x*y}")
keyword_only(x=5, y=10)
# keyword_only(5,10)  # This will raise a TypeError

def mix_params(a, b, /, c=1,*,  d=2):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
mix_params(1, 2, c=3, d=4)
mix_params(5, 6)  # uses default c and d