# product_filter.py

class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_by_price(self, min_price=None, max_price=None):
        filtered_products = []
        for product in self.products:
            if (min_price is None or product.price >= min_price) and (max_price is None or product.price <= max_price):
                filtered_products.append(product)
        return filtered_products

    def filter_by_brand(self, brand):
        filtered_products = []
        for product in self.products:
            if product.brand.lower() == brand.lower():
                filtered_products.append(product)
        return filtered_products

    def filter_by_processor(self, processor):
        filtered_products = []
        for product in self.products:
            if product.processor.lower() == processor.lower():
                filtered_products.append(product)
        return filtered_products

    def filter_by_screen_size(self, min_size=None, max_size=None):
        filtered_products = []
        for product in self.products:
            if (min_size is None or product.screen_size >= min_size) and (max_size is None or product.screen_size <= max_size):
                filtered_products.append(product)
        return filtered_products

    def filter_by_device_type(self, device_type):
        filtered_products = []
        for product in self.products:
            if product.device_type.lower() == device_type.lower():
                filtered_products.append(product)
        return filtered_products
