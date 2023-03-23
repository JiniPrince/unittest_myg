import pytest
from  Addto_cart.addto_cart.addto_cart import Cart,Product

@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def product():
    return Product(name='REALME', description='ANDROID MOBILE', price=9099)

def test_add_to_cart(cart, product):
    quantity = 2
    cart.add_to_cart(product, quantity)
    assert len(cart.cart_items) == 1
    assert cart.cart_items[0]['product'] == product
    assert cart.cart_items[0]['quantity'] == quantity
