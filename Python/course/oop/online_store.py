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
    def reduce_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        else:
            return False
    
class Electronics(Product):
    def apply_discount(self): 
        self._price *= 0.90  #self._price - (self._price * 0.10)

class Clothing(Product):
    def apply_discount(self): 
        self._price *= 0.80  #self._price - (self._price * 0.20)

class Grocery(Product):
    def apply_discount(self): 
        self._price *= 0.90  
   

class ShoppingCart:
    def __init__(self):
        self.items = {} #dictionary

    def add_to_cart(self, product: Product, quantity):
        if product.reduce_stock(quantity):
            self.items[product.name] = {
                'product': product,
                'quantity': quantity }
        else: 
            print(f"Not enough stock for {product.name}")
    
    def __str__(self):
        if not self.items:
            return "Cart is empty!"
        else:
            message = ""
            for key, value in self.items.items():
                message+= f"\n{value['quantity']}x {key} \t ${value['product'].get_price()}\n"
            return f"Items in cart: {message}"
        
        
#Create products      
laptop = Electronics("Laptop", 10000,100)
tshirt = Clothing("TShirt", 1000,20)
apple = Grocery("Apple", 20,10)

print(f"-----------\nThe products list\n---------------")
print(laptop)
print(tshirt)
print(apple)

#create Shopping cart
cart = ShoppingCart()
print(cart)
cart.add_to_cart(laptop, 1)
cart.add_to_cart(apple, 2)
print(cart)

