def sum(x,y):
    return x + y
result1 = sum(10, 20)
result2 = sum("Hello, ", "World!")
result3 = sum([1, 2, 3], [4, 5, 6])  # This will work and return [1, 2, 3, 4, 5, 6]
result4 = sum(1.1, 2.6)  # This will work and return 3.7
print("Sum of integers:", result1)
print("Sum of strings:", result2)
print("Sum of lists:", result3)
print("Sum of floats:", result4)

def sub(x,y):
    pass  # Function does nothing