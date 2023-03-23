#cart_function.py
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_quantity(self, item, quantity):
        item['quantity'] = quantity

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item['price'] * item['quantity']
        return subtotal

    def calculate_taxes(self):
        return self.calculate_subtotal() * 0.1

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_taxes()
