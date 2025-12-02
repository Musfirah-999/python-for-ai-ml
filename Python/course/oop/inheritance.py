# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display_info(self):
#      print(f"{self.name} is {self.age} years old.")
     
# class Employee(Person):
#     pass

    
# employee1 = Employee("Ali", 25)
# employee1.display_info()
# employee1.age = 30
# employee1.display_info()

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    pass

class Bird(Animal):
    pass
class Reptile(Animal):
    pass

cat = Mammal("cat")
cat.eat()

bird = Bird("Parrot")
bird.sleep()