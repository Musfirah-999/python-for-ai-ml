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
    def make_sound(self):
        print(f"{self.name} aminal is making sound.")

class Mammal(Animal):
    def __init__(self, name,fur_type):
        super().__init__(name)
        self.fur_type = fur_type
    def nurse(self):
        print(f"{self.name} is nursing.")
        
    def make_sound(self):
        super().make_sound()
        #  Animal.make_sound(self)
        print(f"{self.name} mammal is making sound.")
        
class Dog(Mammal):
    
    def fetch(self):
        print(f"{self.name} is fetching a ball.")
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} dog is barking.")
        # Animal.make_sound(self)

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.") 
    def build_nest(self):
        print(f"{self.name} is building nest.") 
class Reptile(Animal):
    def hiberate(self):
        print(f"{self.name} is hiberating.") 
        

# cat = Mammal("Cat")
# cat.eat()
# cat.nurse()

# bird = Bird("Parrot")
# bird.sleep()
# bird.build_nest()
# bird.fly()

# reptile = Reptile("Spooky")
# reptile.eat()
# reptile.hiberate()


# myAnimal = Mammal("Cat", "Curly fur")
# myAnimal.make_sound()
# myAnimal.fur_type = "Double coat"

myDog = Dog("Puppy", "Wavy fur")
# myDog.nurse()
# myDog.sleep()
# myDog.fetch()
myDog.make_sound()
myDog.fur_type= "Wool coat"

# yourAnimal = Animal("Your pet")
# yourAnimal.make_sound()