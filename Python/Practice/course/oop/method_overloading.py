# class MAthOperation:
#     def add(self, x, y, z):
#         return x + y+ z
    
#     def add(self, x, y, z=0):
#         return x + y

# math = MAthOperation()
# print(f"10 + 20 = {math.add(10,20)}")
# print(f"10 + 20 + 30 = {math.add(10,20,30)}")


class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return Book(self.pages + other.pages)
    
    def __eq__(self, other):
        return self.pages == other.pages
    
    def __str__(self):
        return f"Book with {self.pages} pages!"
  
          
book1 = Book(150)
book2 = Book(100)
book3 = book1 + book2
print(book3)
print(book1 == book2)