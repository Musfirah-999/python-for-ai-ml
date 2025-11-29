# def hello():
#     print("Hello, World!")

# def show_message(message):
#     print(message)

# def sum(a:int,b:int):
#     # print(a+b)
#     return a+b

# hello()
# x = "Hello"
# y = ", World!"
# a = 10
# b =10
# print(a, "+",b , " is: ", sum(a,b))
# print("Concatenation: ", sum(x,y))
# show_message(x)
# # sum("hello", 5) # TypeError: can only concatenate str (not "int") to str
# # sum(10, "5") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# # sum([1,2], [3,4])  # This will work and return [1, 2, 3, 4]
# # print("Sum of lists: ", sum([1,2], [3,4]))
# # sum((1,2), (3,4))  # This will work and return (1, 2, 3, 4)
# # print("Sum of tuples: ", sum((1,2), (3,4)))
# sum()

#------------optional parameters-----------------
def greet(name="Guest"):
    print("Hello,", name)
greet("Alice")
greet()  # Uses default parameter


#------------keyword parameters-----------------
def display_info(name, age):
    print("Name:", name)
    print("Age:", age)
    
display_info(age=30, name="Bob")  # Using keyword arguments