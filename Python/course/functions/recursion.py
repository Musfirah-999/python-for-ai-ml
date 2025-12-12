#
# def calculateFactorial(n): #iterative approach
#     result = 1
#     for i in range(1, n):
#         result *= i
#     return result
# n = int(input("Enter a number to calculate its factorial: "))
# print(f"Factorial of {n} is:", calculateFactorial(n))

def factorial(n): #recursive approach
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {n} is:", factorial(n))