import pytest
from  CartFuction.cart_function.cart_function import Cart

@pytest.fixture
def cart():
    return Cart()


def test_add_item(cart):
    cart.add_item({'name': 'Laptop', 'price': 1000, 'quantity': 1})
    assert len(cart.items) == 1


def test_remove_item(cart):
    item = {'name': 'Laptop', 'price': 1000, 'quantity': 1}
    cart.add_item(item)
    cart.remove_item(item)
    assert len(cart.items) == 0


def test_update_quantity(cart):
    item = {'name': 'Laptop', 'price': 1000, 'quantity': 1}
    cart.add_item(item)
    cart.update_quantity(item, 2)
    assert item['quantity'] == 2


def test_calculate_subtotal(cart):
    cart.add_item({'name': 'Laptop', 'price': 1000, 'quantity': 2})
    cart.add_item({'name': 'Keyboard', 'price': 50, 'quantity': 1})
    assert cart.calculate_subtotal() == 2050

def test_calculate_taxes(cart):
    cart.add_item({'name': 'Laptop', 'price': 1000, 'quantity': 2})
    cart.add_item({'name': 'Keyboard', 'price': 50, 'quantity': 1})
    assert cart.calculate_taxes() == 205


def test_calculate_total(cart):
    cart.add_item({'name': 'Laptop', 'price': 1000, 'quantity': 2})
    cart.add_item({'name': 'Keyboard', 'price': 50, 'quantity': 1})
    assert cart.calculate_total() == 2255
