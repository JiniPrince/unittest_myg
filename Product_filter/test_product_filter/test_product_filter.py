# test_product_filter.py

import pytest
from Product_filter.product_filter.product_filter import ProductFilter
class Product:
    def __init__(self, name, brand, price, processor, screen_size, device_type):
        self.name = name
        self.brand = brand
        self.price = price
        self.processor = processor
        self.screen_size = screen_size
        self.device_type = device_type

products = [
    Product('iPhone 13', 'Apple', 999, 'A15 Bionic', 6.1, 'smartphone'),
    Product('Samsung Galaxy S21', 'Samsung', 799, 'Exynos 2100', 6.2, 'smartphone'),
    Product('Dell XPS 13', 'Dell', 1099, 'Intel Core i7', 13.4, 'laptop'),
    Product('Lenovo ThinkPad X1 Carbon', 'Lenovo', 1399, 'Intel Core i5', 14, 'laptop'),
    Product('Samsung Galaxy Tab S7', 'Samsung', 649, 'Snapdragon 865+', 11, 'tablet')
]

@pytest.fixture
def product_filter():
    return ProductFilter(products)

def test_filter_by_price(product_filter):
    filtered_products = product_filter.filter_by_price(min_price=800)
    assert len(filtered_products) == 3
    assert filtered_products[0].name == 'iPhone 13'
    assert filtered_products[1].name == 'Dell XPS 13'

def test_filter_by_brand(product_filter):
    filtered_products = product_filter.filter_by_brand('Samsung')
    assert len(filtered_products) == 2
    assert filtered_products[0].name == 'Samsung Galaxy S21'
    assert filtered_products[1].name == 'Samsung Galaxy Tab S7'

def test_filter_by_processor(product_filter):
    filtered_products = product_filter.filter_by_processor('intel core i7')
    assert len(filtered_products)
