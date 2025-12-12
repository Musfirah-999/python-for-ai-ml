# def add(x:int,y:int) -> int:
#     return x + y
# print(add(2, 3))

# def greet(name: str) -> str:
#     return f"Hello, {name}!"

# result = greet("Alice")
# print(result)

# def get_coordinates() -> tuple[float, float]:
#     return (10.0, 20.0)

# coords = get_coordinates()
# print(coords)  # Output: (10.0, 20.0)

# def get_numbers() -> list[int]:
#     return [1, 2, 3, 4, 5]

# numbers = get_numbers()
# print(numbers)  # Output: [1, 2, 3, 4, 5]

# def get_user_info() -> dict[str, str]:
#     return {"name": "Alice", "age": "30"}
# user_info = get_user_info()
# print(user_info)  # Output: {'name': 'Alice', 'age': '30'}

# from typing import Union
# def get_data(flag) -> Union[str, None]:
#     if flag:
#         return "Data loaded"
#     else:
#         return None
# data = get_data(False)
# print(data)  # Output: None

from typing import Callable
def multiply(a: int) -> Callable[[int], int]:
    def multiplier(b: int) -> int:
        return a * b
    return multiplier

multiply_by_3 = multiply(3)
print(multiply_by_3(10))  # Output: 30

