#search.py
class Product_search:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class Myg_store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search_products(self, keyword=None, category=None):
        matching_products = []
        for product in self.products:
            if keyword and keyword.lower() in product.name.lower():
                matching_products.append(product)
            elif category and category.lower() == product.category.lower():
                matching_products.append(product)
        return matching_products
