class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price #protected attribute
        self._stock = stock
    
    def get_price(self):
        return self._price

    def apply_discount(self):
        raise NotImplementedError("Sub classes must implement this method...")
    
    def __str__(self):
        return f"{self.name}: ${self._price}\t Stock: {self._stock}"
    
class Electronics(Product):
    def apply_discount(self): 
        self._price *= 0.90  #self._price - (self._price * 0.10)

class Clothing(Product):
    def apply_discount(self): 
        self._price *= 0.80  #self._price - (self._price * 0.20)

class Grocery(Product):
    def apply_discount(self): 
        self._price *= 0.90  
        
        
laptop = Electronics("Laptop", 10000,10)
tshirt = Clothing("TShirt", 1000,20)
apple = Grocery("Apple", 20,10)

print(f"-----------\nThe products list\n---------------")
print(laptop)
print(tshirt)
print(apple)
