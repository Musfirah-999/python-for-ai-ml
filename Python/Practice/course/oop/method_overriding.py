class Animal:
    def make_sound(self):
        print(f"Animal is making sound.")

class Dog(Animal):
    def make_sound(self):
        print(f"Dog is barking.")
        
class Cat(Animal):
    def make_sound(self):
        print(f"Cat meows.")
    

animals = [Dog(), Cat(), Animal()]
# cat =Cat()
# dog = Dog()
# animal = Animal()
# animals = [dog, cat, animal]

for animal in animals:
    animal.make_sound()

