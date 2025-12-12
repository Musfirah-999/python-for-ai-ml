# def sum(x,y):
#     return x + y


# sum_lambda = lambda x,y: x + y  # Anonymous function (lambda) that adds two numbers
# result1 = sum(10, 20)
# print("Sum of integers:", result1)
# result2 = sum_lambda(15, 25)
# print("Sum using lambda:", result2)


# square = lambda x: x ** 2  # Lambda function to calculate square
# num = 5
# result3 = square(num)
# print(f"Square of {num} is:", result3)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))  # Using lambda with map to square each number in the list
print("Squared numbers:", squared_numbers)

even_lambda = lambda x: x % 2 == 0  # Lambda function to check if a number is even
numbers = filter(even_lambda, numbers)  # Using lambda with filter to get even numbers
print("Even numbers:", list(numbers))

