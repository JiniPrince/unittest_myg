#addto_cart.py
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        item = {'product': product, 'quantity': quantity}
        self.cart_items.append(item)

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
