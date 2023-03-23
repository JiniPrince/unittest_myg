#signup.py
def sign_up(email, password):
    # Validate email
    if '@' not in email:
        raise ValueError('Invalid email')

    # Validate password
    if len(password) < 6:
        raise ValueError('Password too weak')
    #sign up a Registerd user then return success
    return 'Success'
