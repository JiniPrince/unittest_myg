import pytest
from User_profile.userprofile.userprofile import UserProfile
@pytest.fixture
def user_profile():
    return UserProfile()

def test_view_profile(user_profile):
    assert user_profile.view_profile() == {'name': '', 'shipping_address': {}}

def test_update_name(user_profile):
    user_profile.update_name('Jini', 'Prince')
    assert user_profile.name == 'Jini Prince'

def test_update_shipping_address(user_profile):
    shipping_address = {
        'address': 'Hanna Cottage',
        'city': 'Chirayinkeezhu',
        'country': 'India',
        'state': 'Kerala',
        'postal_code': '695304',
        'phone': '917012601404',
        'signup_newsletter': True
    }
    user_profile.update_shipping_address(shipping_address)
    assert user_profile.shipping_address == shipping_address
