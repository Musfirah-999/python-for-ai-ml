from abc import ABC,abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
    
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14*self.radius*self.radius

# circle = Circle(10)
# area = circle.area()
# print(area)


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
    def move(self):
        print("Dog is runnig.")
        
class Bird(Animal):
    def make_sound(self):
        print("Bird is chirping.")
    def move(self):
        print("Bird is flying.")
        
bird = Bird()
bird.make_sound()
bird.move()

dog = Dog()
dog.move()
dog.make_sound()

# animal = Animal()   #not allowed