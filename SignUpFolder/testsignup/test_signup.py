#test_signup.py
from SignUpFolder.signup.signup import sign_up
import pytest
def test_sign_up():
    # Test case 1: Verify that the function returns 'Success' for valid input.
    result = sign_up('jiniprince@gmail.com', 'password123')
    assert result == 'Success'

    # Test case 2: Verify that the function raises a ValueError for an invalid email.
    with pytest.raises(ValueError):
        sign_up('jiniprince', 'password123')

    # Test case 3: Verify that the function raises a ValueError for a weak password.
    with pytest.raises(ValueError):
        sign_up('jiniprince@gmail.com', '123')
