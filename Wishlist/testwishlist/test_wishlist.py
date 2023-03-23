# test_wishlist.py

import pytest
from Wishlist.wishlist.wishlist import Wishlist
@pytest.fixture
def wishlist():
    return Wishlist()

def test_add_item(wishlist):
    wishlist.add_item('item1')
    assert 'item1' in wishlist.items

def test_remove_item(wishlist):
    wishlist.add_item('item1')
    wishlist.remove_item('item1')
    assert 'item1' not in wishlist.items

def test_clear_wishlist(wishlist):
    wishlist.add_item('item1')
    wishlist.add_item('item2')
    wishlist.clear_wishlist()
    assert len(wishlist.items) == 0
