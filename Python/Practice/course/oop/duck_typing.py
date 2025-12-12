class Dog:
    def make_sound(self):
        print("Woof!")
        
class Cat:
    def make_sound(self):
        print("Meow!")
        
class Duck:
    def make_sound(self):
        print("Quack!")

def animal_sound(animal):
    animal.make_sound()
    

dog = Dog()
cat = Cat()
duck = Duck()
animal_sound(dog)
animal_sound(cat)
animal_sound(duck)
