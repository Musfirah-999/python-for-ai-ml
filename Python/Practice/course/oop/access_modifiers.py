# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating.")
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#     def make_sound(self):
#         print(f"{self.name} aminal is making sound.")
    
# class Dog(Animal):
    # def __init__(self, name, fur_type):
    #     super().__init__(name)
    #     self.fur_type = fur_type
    
    # def fetch(self):
    #     print(f"{self.name} is fetching a ball.")
    # def make_sound(self):
    #     super().make_sound()
    #     print(f"{self.name} dog is barking.")
        # Animal.make_sound(self)

# dog = Dog("Buddy", "Curly fur")
# print(f"Dog name is {dog.name}")
# dog.make_sound()

# class Animal:
#     def __init__(self,name):
#         self._name = name
#     def _make_sound(self): #protected method
#         print(f"{self._name} aminal is making sound.")
    
# class Dog(Animal):
#     def __init__(self, name, fur_type):
#         super().__init__(name)
#         self.fur_type = fur_type
    
#     # def fetch(self):
#     #     print(f"{self.name} is fetching a ball.")
#     # def make_sound(self):
#     #     super().make_sound()
#     #     print(f"{self.name} dog is barking.")
#         # Animal.make_sound(self)
#     def show_name(self):
#         print(f"Dog name is {self._name}") #allowed
        

# dog = Dog("Buddy", "Curly fur")
# print(f"Dog name is {dog._name}")
# dog.show_name()
# dog._make_sound() #allow but not recommended


class Animal:
    def __init__(self,name):
        self.__name = name #private attribute
    def __make_sound(self): #private method
        print(f"{self.__name} aminal is making sound.")
    
    
class Dog(Animal):
    def __init__(self, name, fur_type):
        super().__init__(name)
        self.fur_type = fur_type
    
    def show_name(self):
        print(f"Dog name is {self._Animal__name}")  #name mangling
        

dog = Dog("Buddy", "Curly fur")
dog.show_name()
# dog.__make_sound() #allow but not recommended