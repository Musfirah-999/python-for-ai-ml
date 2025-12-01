class Student:
    name = "John Doe"
    age = 20
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
student1 = Student("John Doe", 20)
print("Student Name:", student1.name)
student2 = Student("Jane Smith", 22)

print("Student Name:", student2.name)

class Car:
    def __init__(self,model, year):
        self.model = model
        self.year = year
    def display_info(self):
        return f"Car Model: {self.model}, Year: {self.year}"

myCar = Car("Toyota", 2020)
print(myCar.display_info())