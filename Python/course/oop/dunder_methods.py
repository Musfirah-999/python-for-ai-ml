#pre-defined dunder methods in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def __str__(self):
        return f"{self.name}, {self.age}"
    
person1 = Person("Alice", 30)
print(f"Person1 is {person1}")
print(person1.greet())