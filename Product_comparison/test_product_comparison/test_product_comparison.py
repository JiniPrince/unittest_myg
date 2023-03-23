# test_product_comparison.py

import pytest
from Product_comparison.product_comparison.product_comparison import ProductComparison
@pytest.fixture
def product_comparison():
    return ProductComparison()

def test_add_product(product_comparison):
    product_comparison.add_product('product1')
    assert 'product1' in product_comparison.products

def test_remove_product(product_comparison):
    product_comparison.add_product('product1')
    product_comparison.remove_product('product1')
    assert 'product1' not in product_comparison.products

def test_compare_products_not_enough_products(product_comparison):
    result = product_comparison.compare_products()
    assert result == "Please add at least two products to compare."

def test_compare_products_enough_products(product_comparison):
    product_comparison.add_product('product1')
    product_comparison.add_product('product2')
    result = product_comparison.compare_products()
    assert result == "Comparison complete."
