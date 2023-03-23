import pytest

from Product_display.product_display.product_display import ProductDisplay
@pytest.fixture
def product_display():
    return ProductDisplay()

def test_display_products(product_display):
    products = product_display.display_products()
    for product in products:
        assert 'name' in product
        assert 'description' in product
        assert 'price' in product
        assert 'image' in product
        assert 'reviews' in product
        assert 'features' in product
