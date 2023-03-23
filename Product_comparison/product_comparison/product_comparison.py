# product_comparison.py

class ProductComparison:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def compare_products(self):
        if len(self.products) < 2:
            return "Please add at least two products to compare."
        else:
            return "Comparison complete."

