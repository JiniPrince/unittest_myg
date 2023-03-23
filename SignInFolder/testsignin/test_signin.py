
#test_signin.py

from SignInFolder.signin.signin import signin,send_otp
import pytest

def test_valid_credentials():
    # Test valid credentials
    result = signin("Jini", "Prince", "7012601404", "jinixalbert18@gmail.com", "password123", "password123")
    assert result == True

def test_invalid_firstname():
    # Test invalid firstname
    result = signin("", "Prince", "7012601404", "jinixalbert18@gmail.com", "password123", "password123")
    assert result == False

def test_invalid_lastname():
    # Test invalid lastname
    result = signin("Jini", "", "7012601404", "jinixalbert18@gmail.com", "password123", "password123")
    assert result == False

def test_invalid_phone():
    # Test invalid phone number
    result = signin("Jini", "Prince", "1234", "jinixalbert18@gmail.com", "password123", "password123")
    assert result == False

def test_invalid_email():
    # Test invalid email
    result = signin("John", "Prince", "1234567890", "jiniprince", "password123", "password123")
    assert result == False

def test_password_mismatch():
    # Test password mismatch

    result = signin("Jini", "Prince", "7012601404", "jinixalbert18@gmail.com", "password123", "password456")
    assert result == False

def test_send_otp_with_valid_otp():
    result = send_otp("1234567890", "1234")
    assert result == True


def test_send_otp_with_invalid_otp():
    result = send_otp("1234567890", "5678")
    assert result== True


def test_send_otp_timeout():
    result=send_otp("1234567890", "1234")
    assert result==True

#pytest --capture=no testsignin/test_signin.py
