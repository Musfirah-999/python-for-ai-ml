class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price  # protected attribute
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
        return self._price * 0.90  # self._price - (self._price * 0.10)


class Clothing(Product):
    def apply_discount(self):
        return self._price * 0.80  # self._price - (self._price * 0.20)


class Grocery(Product):
    def apply_discount(self):
        return self._price


class ShoppingCart:
    def __init__(self):
        self.items = {}  # dictionary

    def add_to_cart(self, product: Product, quantity):
        if product.reduce_stock(quantity):
            if product.name in self.items:
                self.items[product.name]['quantity']+=quantity
            else:
                self.items[product.name] = {
                'product': product,
                'quantity': quantity}
        else:
            print(f"Not enough stock for {product.name}")

    def calculate_total_price(self):
        total_price = 0
        for item in self.items.values():
            product: Product = item['product']
            # product.apply_discount()
            # total_price +=product.get_price()*item['quantity']
            total_price += product.apply_discount()*item['quantity']
        return total_price

    def check_out(self):
        if not self.items:
            print("Cart is empty!")
            return
        print("---------\nCheckout Summary:")
        message = ""
        for key, value in self.items.items():
            message += f"\n{value['quantity']}x {key} \t ${value['product'].get_price()}"
        print(message)
        print(f"TOtal price: ${self.calculate_total_price()}")
        print(f"Thanks for shopping")
        self.items.clear()

    def __str__(self):

        message = "--------\n-------Shopping Cart--------\n"
        if not self.items:
            message += "Cart is empty!"

        else:
            for key, value in self.items.items():
                message += f"\n{value['quantity']}x {key} \t ${value['product'].apply_discount()}"
            # message+= f"Items in cart: \n{message} \nTotalPrice: ${self.calculate_total_price()}"
            message += "\n-------------\n"
        return message


# Create products
laptop = Electronics("Laptop", 10000, 100)
tshirt = Clothing("TShirt", 1000, 20)
apple = Grocery("Apple", 20, 10)

print(f"-----------\nThe products list\n---------------")
print(laptop)
print(tshirt)
print(apple)

# create Shopping cart
cart = ShoppingCart()
print(cart)
cart.add_to_cart(laptop, 1)
cart.add_to_cart(laptop, 3)
cart.add_to_cart(apple, 2)
print(cart)
cart.check_out()
print(cart)
